drop database if exists WSChampions;
CREATE DATABASE WSChampions;

USE WSChampions;
-- 5A (Team, Player)
-- 7C: seen throughout each attribute creation
-- 7D: seen throughout each attribute creation
CREATE TABLE Team(
	TeamName VARCHAR(50) NOT NULL, 
    YearDate SMALLINT UNSIGNED NOT NULL,
    TotalRunScored SMALLINT UNSIGNED NOT NULL DEFAULT '0',
    TotalHits SMALLINT UNSIGNED NOT NULL DEFAULT '0',
    TotalOPS FLOAT(4, 3) UNSIGNED NOT NULL DEFAULT '0',
    PRIMARY KEY (YearDate)
);
-- 5A
CREATE TABLE Player(
    PlayerName VARCHAR(60) NOT NULL,
    PlayerTeam VARCHAR(50) NOT NULL,
    Position VARCHAR(3) NOT NULL,
    PlayerYear SMALLINT UNSIGNED,
    PRIMARY KEY (PlayerName, PlayerTeam, PlayerYear),
    -- 6A
    FOREIGN KEY (PlayerYear) REFERENCES Team(YearDate)
         ON DELETE RESTRICT
         ON UPDATE CASCADE
	
);
-- 5C (Stats)
-- 7A 
CREATE TABLE Stats(
    -- 5B (StatYear)
    StatYear SMALLINT UNSIGNED NOT NULL,
    PlayerName VARCHAR (60) NOT NULL,
    PlayerTeam VARCHAR (60) NOT NULL, 
    AtBats SMALLINT UNSIGNED NOT NULL DEFAULT '0',
    Hits SMALLINT UNSIGNED NOT NULL DEFAULT '0',
    OPS FLOAT(4,3) UNSIGNED NOT NULL DEFAULT '0.000',
    Runs SMALLINT UNSIGNED NOT NULL DEFAULT '0',
    PlateAppearances SMALLINT UNSIGNED NOT NULL DEFAULT '0',
    -- 6A
    FOREIGN KEY (StatYear) REFERENCES Player(PlayerYear)
        -- 7B
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    
	-- 6B
    FOREIGN KEY (StatYear) REFERENCES Team(YearDate)
        -- 7B
        ON DELETE CASCADE
        ON UPDATE CASCADE
    
);
-- 6C no many-many relationships
-- 5D no direct supertype/subtype entities currently

-- Run the following commands to check data has been pushed (after connecting & using the sql.python file)
