import sys
import sqlite3
from datetime import datetime


class PDBC:
    conn = None

    def getID(self, ip):

        # Creating a cursor object
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT ID FROM device WHERE IP=?",(ip,))
        rows = self.cursor.fetchone()
        self.cursor.close()
        if not rows:
            return 0

        return rows.get('value')

    def getLastID(self):

        # Creating a cursor object
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT MAX(ID) FROM device ")
        rows = self.cursor.fetchone()
        self.cursor.close()
        if not rows:
            return 0
        return rows.get('value')

    def newDevice(self, ip, shard, device_id):

        # Creating a cursor object
        self.cursor = self.conn.cursor()
        sql = '''INSERT INTO device(ID, shard, IP) VALUES(?,?,?)'''
        self.cursor.execute(sql, (device_id, shard, ip ))
        self.cursor.close()
        self.conn.commit()

    def close(self):
        print("Closing database...")

        self.cursor.close()
        self.conn.close()

        print("Successfully closed connection to database!")

    def __init__(self, dbName: str):
        # Establishing the connection
        self.conn = sqlite3.connect(dbName)

        print("Successfully connected to database %s" % dbName)

        # Creating a cursor object
        self.cursor = self.conn.cursor()

        print("Done! Database is ready to use")


class Log:
    def __init__(self, file):
        self.file = open(file, "a")

    def log(self, msg):
        self.file.write("[" + self.timestamp() + "] - " + msg + "\n")

    def close(self):
        self.file.close()

    def timestamp(self):
        return datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')

