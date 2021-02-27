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
        sql = ''' INSERT INTO projects(name,begin_date,end_date) VALUES(?,?,?) '''
        self.cursor.execute(sql, (0,0,'0'))
        self.conn.commit()
        print("Done! Database is ready to use")
