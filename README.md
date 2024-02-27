# CIS3103-Project-AllyRyan
CIS-3103-Database Program Development Final Project 
We connect baseball statistics to a World Series Championship. We use the Red Sox statistics from the last three World Series Championship years. We keep track of team, player, and statistics. Each team has players, aggregate statistics, and a year. Each player has a name, jersey number, and year. The statistics we value are number of hits, on base percentage, and number of runs. Each team has up to 26 players. Each player must have a unique jersey number in each year. Each jersey number must be 1 or 2 digits. We are seeking to find three minimum values (hits, runs, OPS) that win a team (Red Sox in particular) a World Series. 

# Entities, relationships, attributes
## Entity 1 - Team
Attributes 
- Year PRIMARY KEY
- Total runs scored 
- Total hits collected 
- Total OPS 

## Entity 2 - Player
Attributes
    - Name
    - JerseyNumber
    - Year FOREIGN KEY

## Entity 3 - Statistics
Attributes
- Hits
- OPS (On base percentage + slugging)
- Runs

## Relationships
Team-Includes-Player
Player-Has-Statistics
Team-Has-Statistics

# Glossary Information
## Attribute types
- Name: NAME
- JerseyNumber: SMALLINT UNSIGNED
- Year: DATE
- Hits: SMALLINT UNSIGNED
- OPS: FLOAT(4, 3) UNSIGNED
- Runs: SMALLINT UNSIGNED
- Total runs scored: SMALLINT UNSIGNED
- Total hits collected: SMALLINT UNSIGNED
- Total OPS: FLOAT(4, 3) UNSIGNED


## Document names, synonyms, descriptions
- Name/playerName - Name of player on Red Sox
- JerseyNumber - The number the player wears when he plays
- Year/date - year of the specific team, year a specific player was on that year's team
- Hits/basehit - a statistic describing a basehit in baseball
- OPS/on base plus slugging - on base plus slugging is a calculated statistic that combines on base percentage with slugging percentage
- Runs - the number of times a player crosses home plate to score a run for the Red Sox
- Total runs scored - a sum of all runs scored by each player for a specific year
- Total hits collected - a sum of all the hits collected by each player for a specific year
- Total OPS - calculated average OPS (on base plus slugging) between all players for a specific year

## Description of Data
The data includes three csv files that each contain extended statistics for the Red Sox in their latest 3 World Series Championships (2007,2013, 2018). The data includes values as listed in the following line
    Rk,Pos,Name,Age,G,PA,AB,R,H,2B,3B,HR,RBI,SB,CS,BB,SO,BA,OBP,SLG,OPS,OPS+,TB,GDP,HBP,SH,SF,IBB,Name-additional

