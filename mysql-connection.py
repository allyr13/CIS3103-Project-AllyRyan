import mysql.connector
from mysql.connector import errorcode
import csv
import os
import json
import sys

def getConfigFile():
    if __name__ == "__main__":  
        ## Get the configuration file 
        configFileLocation = sys.argv[1]  
        print("Configuration file location: {0}".format(configFileLocation))   
        configFile = open(configFileLocation)
        configFileJSON = json.load(configFile)
        return configFileJSON
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


def insertTeam(name, year, runs, hits, ops):
    val = "INSERT INTO Team VALUES ('" + name + "'," + str(year) + "," + str(runs) + "," + str(hits) + "," + "{:.3f}".format(ops) + ");"
    print(val)
    return val

def insertPlayer(name, playerTeam, position, year):
    val = "INSERT INTO Player VALUES ('" + name + "','" + playerTeam + "','" + position + "'," + str(year) + ");"
    print(val)
    return val

def getFiles(folderPath):
    # For loop through each data file in "Data" folder
    path = folderPath
    dir_list = os.listdir(path) 
    return dir_list

def addAllTeams(item):
    with open('./Data/' + item, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        totalRuns = 0
        totalHits = 0
        totalOPS = 0.0
        rows = 0
        for row in reader:
            runs = row['R']
            totalRuns = totalRuns + int(runs)
            totalHits = totalHits + int(row['H'])
            if (row['OPS']!= ''):
                ops = row['OPS']
            
            totalOPS = totalOPS + float(ops)
            rows = rows + 1

        totalOPS = totalOPS / rows
        playerTeam = item[0:4]
        periodIdx = item.index(".")
        playerYear = item[4:periodIdx]
        team = insertTeam(playerYear, playerTeam, totalRuns, totalHits, totalOPS)
        teamCursor.execute(team)
        print("Team executed to DB")

def addAllPlayers(item):
    with open('./Data/' + item, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name']
            pos = row['Pos']
            playerYear = item[0:4]
            periodIdx = item.index(".")
            playerTeam = item[4:periodIdx]
            player = insertPlayer(name,playerTeam,pos,playerYear)
            teamCursor.execute(player)
            print("Player executed to DB")
            #print(row['Rk'], row['Pos'])

def executeToDatabase(dir_list):
    for item in dir_list:
        addAllTeams(item)
        addAllPlayers(item)


executeToDatabase(getFiles('./Data'))

reservationConnection.commit()
teamCursor.close()
