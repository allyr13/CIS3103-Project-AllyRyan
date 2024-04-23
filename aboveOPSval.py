import mysql.connector
from mysql.connector import errorcode
import csv
import os
import json
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def getConfigFile():
    if __name__ == "__main__": 
        try:
            with open('config.json') as configFile:
                configFileJSON = json.load(configFile)
            return configFileJSON
        except FileNotFoundError:
            print("Config file not found.")
            sys.exit(1) 

    else:
        configjson = {
            "user": "root",
            "password": "redsox2004!",
            "host": "127.0.0.1",
            "database": "WSChampions"
        }
        return configjson

try:
    config = getConfigFile()
    reservationConnection = mysql.connector.connect(**config)
    teamCursor = reservationConnection.cursor()
    
    

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Invalid credentials')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('Databse not found')
    else:
        print('Cannot connect to database:', err)

teamCursor = reservationConnection.cursor()

queryOver1000 = "SELECT Team.TeamName, Team.YearDate,COUNT(*) AS PlayerAbv900OPS FROM Team INNER JOIN Player ON Team.YearDate = Player.PlayerYear INNER JOIN Stats ON Player.PlayerName = Stats.PlayerName AND Player.PlayerTeam = Stats.PlayerTeam WHERE Stats.OPS > 1.00 AND Team.TeamName = Stats.PlayerTeam GROUP BY Team.TeamName, Team.YearDate ORDER BY Team.YearDate;"


teamCursor.execute(queryOver1000)
data = teamCursor.fetchall()

for i in data:
    print (i)




df = teamCursor.fetchall()
df = pd.DataFrame(data, columns=['TeamName', 'YearDate', 'PlayerAbv900OPS'])
for i, row in df.iterrows():
    plt.title('2000-2023 Players Above .900OPS', fontsize=20)
        # Create label for x-axis, font size set to 14
    plt.xlabel('Year', fontsize=14)
    # Create label for y-axis, font size set to 14
    plt.ylabel('Number of Players Above 900OPS', fontsize=14)

    plt.scatter(row['YearDate'], row['PlayerAbv900OPS'], label=row['TeamName'])
plt.legend()
plt.show()
plt.savefig('Number of Players Above 1.000OPS')
reservationConnection.commit()
teamCursor.close()