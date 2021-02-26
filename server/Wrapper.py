import sys
import sqlite3


class PDBC:
    conn = None

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
