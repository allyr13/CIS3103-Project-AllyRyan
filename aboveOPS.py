
import numpy as np
import matplotlib.pyplot as plt 
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

values =[]
# creating the dataset
df = pd.DataFrame(data, columns=['TeamName', 'YearDate', 'PlayerAbv900OPS'])
for i, row in df.iterrows():
    courses = ['TeamName', 'YearDate', 'PlayerAbv900OPS']
    values += [row['YearDate'], row['PlayerAbv900OPS'], row['TeamName']]
    plt.bar(courses, values, color ='maroon', 
		width = 0.4)
    fig = plt.figure(figsize = (10, 5))

# creating the bar plot


plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()

reservationConnection.commit()
teamCursor.close()