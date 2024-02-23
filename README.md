# CIS3103-Project-AllyRyan
CIS-3103-Database Program Development Final Project 

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
Player-Has-Stats



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


## Document names, synonyms, and descriptions

