// Reading the file using default
// fs npm package
import {
    DynamoDBClient,
  } from "@aws-sdk/client-dynamodb";
import {
  PutCommand,
  DynamoDBDocumentClient,
} from "@aws-sdk/lib-dynamodb";

import { v4 as uuidv4 } from 'uuid';
import express from "express" // ALWAYS - npm install express needed
import bodyParser from "body-parser";
import fs from 'fs';
import { table } from "console";

const app = express() // ALWAYS
app.use(bodyParser.json());
const log = (msg) => console.log(`[SCENARIO] ${msg}`);
const tableName = "allyryan_db_project"; // Table in DynamoDB

const client = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(client);

function getFiles(folderPath) {
    try {
        const dirList = fs.readdirSync(folderPath);
        return dirList;
    } catch (error) {
        console.error('Error reading directory:', error);
        return [];
    }
}

function CSVToJSON(csvFile, teamName, year){
    let csv = fs.readFileSync(csvFile);
    
    const lines = csv.toString().split('\n'); 
    const keys = lines[0].split(','); 
    return lines.slice(1).map(line => { 
        return line.split(',').reduce((acc, cur, i) => { 
            const toAdd = {}; 
            toAdd['TeamName'] = teamName;
            toAdd['Year'] = year.toString();
            toAdd[keys[i]] = cur; 
            return { ...acc, ...toAdd }; 
        }, {}); 
    }); 
}; 

let allFiles = getFiles("./Data")
let i = 0;

let players;
while (allFiles[i] != null){
    let theFile = "./Data/" + allFiles[i]
    let fileWithoutPath = theFile.substring(7);
    let periodIdx = fileWithoutPath.indexOf(".");
    let yearAndTeam = fileWithoutPath.substring(0, periodIdx);
    let year = yearAndTeam.substring(0,4);
    let team = yearAndTeam.substring(4);

    players = CSVToJSON(theFile, team, year);
    for (let j = 0; j < players.length; j++) {
        let player = players[j];
        //console.log(player.TeamName);
        //console.log(player.Year)
        let playerID = j + 1;
        let numYear = Number(player.Year)
        await updateDB(player, numYear, player.TeamName, playerID);
    }
    i++;
};





async function updateDB(theData, year, teamName, playerID) {
    console.log(year)
    console.log(teamName)
    if (theData == null) {
        const result = {
        status: "Failure - empty body"
        };

        return result;  
    }
        
    const theID = uuidv4();

    const putCommand = new PutCommand({
            TableName: tableName,
            Item: {
                "allyryan_db_project": theID,
                "playerID": playerID.toString(),
                "PlayerName": theData.Name,
                "PlayerTeam" : teamName,
                "Position": theData.PO,
                "PlateAppearances" : theData.PA,
                "RunsScored" : theData.R,
                "OnBasePercentage" : theData.OBP,
                "Hits" : theData.H,
                "AtBats" : theData.AB,
                "Year": year
            },
        });

    try {
            await docClient.send(putCommand);
            console.log("Item added");

            const result = {
            status: "Success"
            };
    
            return result;  
    } catch (err) {
            console.log(err);
            const result = {
            status: "Failure"
            };
    
            return result;  
    }
};







