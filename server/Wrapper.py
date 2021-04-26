import os
import sys
import sqlite3
from datetime import datetime

from Exceptions import UnregisteredDeviceException


class PDBC:
    conn = None

    def insert(self, whenD, machineID, shard, typeD, value, net):
        sql = '''INSERT INTO dataD(whenD, whoMachine, whoShard, typeD, valueD, net) VALUES(?,?,?,?,?,?)'''
        self.cursor.execute(sql, (whenD, machineID, shard, typeD, value, net))

        self.conn.commit()

    def getID(self, ip):
        self.cursor.execute("SELECT ID FROM device WHERE IP=?", (ip,))
        rows = self.cursor.fetchone()

        if not rows:
            raise UnregisteredDeviceException(ip)

        return rows[0]

    def getLastID(self):
        self.cursor.execute("SELECT MAX(ID) FROM device ")
        rows = self.cursor.fetchone()

        if not rows or not rows[0]:
            return 0

        return rows[0]

    def newDevice(self, ip, shard, device_id):
        sql = '''INSERT INTO device(ID, shard, IP) VALUES(?,?,?)'''
        self.cursor.execute(sql, (device_id, shard, ip))

        self.conn.commit()

    def close(self):
        print("Closing database...")

        self.cursor.close()
        self.conn.close()

        print("Successfully closed connection to database!")

    def __init__(self, dbName: str):
        isEmpty = not os.path.exists(dbName)

        # Establishing the connection
        self.conn = sqlite3.connect(dbName, check_same_thread=False)

        print("Successfully connected to database %s" % dbName)

        # Creating a cursor object
        self.cursor = self.conn.cursor()

        if isEmpty:
            print("Oops! The database is empty. Populating...")

            if not os.path.isfile("database.sql"):
                print("But... but... the schema does not exist... Come back with a 'database.sql' or don't come back!")
                self.close()
                os.remove(dbName)

                sys.exit(-1)

            with open("database.sql", 'r') as sqlfile:
                # Put everything into one line
                lines = sqlfile.read().replace("\r\n", "").replace("\n", "")

                # Execute each of the statements
                for statement in lines.split(";"):
                    self.cursor.execute(statement)
                    self.conn.commit()

        print("Done! Database is ready to use")


def timestamp():
    return datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')


class Log:
    def __init__(self, file):
        self.file = open(file, "a")

    def log(self, msg):
        self.file.write("[" + timestamp() + "] - " + msg + "\n")

    def close(self):
        self.file.close()

