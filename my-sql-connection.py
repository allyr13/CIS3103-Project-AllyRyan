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


def insertTeam(name, year):
    val = "INSERT INTO Team (TeamName, YearDate) VALUES ('" + name + "'," + str(year) + ");"
    print(val)
    return val

def insertPlayer(name, playerTeam, position, year):
    val = "INSERT INTO Player VALUES ('" + name + "','" + playerTeam + "','" + position + "'," + str(year) + ");"
    print(val)
    return val

def insertStatistic(statYear, playerName, playerTeam, ab, hits, ops, runs, plateAppearances):
    val = "INSERT INTO Stats (StatYear, PlayerName, PlayerTeam, AtBats, Hits, OPS, Runs, PlateAppearances) VALUES  (" + str(statYear) + ",'" + playerName + "','" + playerTeam + "'," + str(ab) + "," + str(hits) + "," + str(ops)  + "," + str(runs) + "," + str(plateAppearances) + ");"
    print(val)
    return val


def getFiles(folderPath):
    # For loop through each data file in "Data" folder
    path = folderPath
    dir_list = os.listdir(path) 
    return dir_list

def addAllTeams(item):
    with open('./Data/' + item, newline='') as csvfile:
        teamYear = item[0:4]
        periodIdx = item.index(".")
        teamName = item[4:periodIdx]
        team = insertTeam(teamName, teamYear)
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
            player = insertPlayer(name, playerTeam, pos, playerYear)

            teamCursor.execute(player)
            print("Player executed to DB")
            

            #print(row['Rk'], row['Pos'])
def addAllStats(item):
    with open('./Data/' + item, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            playerName = row['Name']
            ops = row['OPS']
            hits = row['H']
            runs = row['R']
            atBats = row['AB']
            plateAppearances = row['AB']
            statYear = item[0:4]
            periodIdx = item.index(".")
            playerTeam = item[4:periodIdx]
            
            statistics = insertStatistic(statYear, playerName, playerTeam, atBats, hits, ops, runs, plateAppearances)
            teamCursor.execute(statistics)
            print("Stats executed to DB")

def executeToDatabase(dir_list):
    for item in dir_list:
        addAllTeams(item)
        addAllPlayers(item)
        addAllStats(item)


executeToDatabase(getFiles('./Data'))

reservationConnection.commit()
teamCursor.close()
