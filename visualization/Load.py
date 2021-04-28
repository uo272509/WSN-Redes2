import os
import sys
import sqlite3
from datetime import datetime
from NonExistentDatabase import NonExistentDatabase
import matplotlib.pyplot as plt
import matplotlib.dates as md
from datetime import datetime
import pandas as pd


def LoadData(dbName: str):
    if not os.path.exists(dbName):
        raise NonExistentDatabase(dbName)

    # Establishing the connection
    conn = sqlite3.connect(dbName)
    # Creating a cursor object
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT whoMachine FROM dataD")
    rows = cursor.fetchall()

    for row in rows:
        whoMachine = row[0]

        cursor.execute("SELECT * FROM dataD WHERE whoMachine=" + str(whoMachine) + " AND whenD>='2021-04-28T14:26:00.915618'")
        data = pd.DataFrame(cursor.fetchall(), columns=["whenD", "whoMachine", "whoShard", "typeD", "valueD", "net"])

        blankIndex = [''] * len(data)
        data.index = blankIndex

        dates = [datetime.strptime(str(s), "%Y-%m-%dT%H:%M:%S.%f") for s in data.whenD]

        y = data.valueD

        plt.clf()
        fig, ax = plt.subplots()
        ax.plot(dates, y, "-")
        ax.set_ylim(0, 100)

        plt.xlabel('Timestamp')
        plt.ylabel('Temperature')
        plt.title(data.typeD[0])

        plt.grid(True)
        plt.gcf().autofmt_xdate()
        plt.show()
        #    print(s)

        #print(dates)
