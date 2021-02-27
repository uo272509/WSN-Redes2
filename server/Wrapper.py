import sys
import sqlite3
from datetime import datetime


class PDBC:
    conn = None

    def getID(self, ip):
        return 0

    def getLastID(self):
        return 0

    def newDevice(self, ip, device_id):
        return 0

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
