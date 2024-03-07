drop database if exists RedSox;
CREATE DATABASE RedSox;

USE RedSox;
-- 5A (Team, Player)
-- 7C: seen throughout each attribute creation
-- 7D: seen throughout each attribute creation
CREATE TABLE Team(
    YearDate SMALLINT UNSIGNED,
    TotalRunScored SMALLINT NOT NULL,
    TotalHits SMALLINT NOT NULL,
    TotalOPS FLOAT(4, 3) NOT NULL,
    PRIMARY KEY (YearDate)
);
-- 5A
CREATE TABLE Player(
    Name VARCHAR(60) NOT NULL,
    JerseyNumber SMALLINT,
    PlayerYear SMALLINT UNSIGNED,
    PRIMARY KEY (PlayerYear, JerseyNumber),
    -- 6A
    FOREIGN KEY (PlayerYear) REFERENCES Team(YearDate)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT
);
-- 5C (Stats)
-- 7A 
CREATE TABLE Stats(
    -- 5B (StatYear)
    StatYear SMALLINT UNSIGNED NOT NULL,
    PlayerName VARCHAR (60) NOT NULL,
    Hits SMALLINT NOT NULL,
    OPS FLOAT(4,3) NOT NULL,
    Runs SMALLINT NOT NULL,
    -- 6A
    FOREIGN KEY (StatYear) REFERENCES Player(PlayerYear)
        -- 7B
        ON DELETE CASCADE
        ON UPDATE RESTRICT,
    
	--6B
    FOREIGN KEY (StatYear) REFERENCES Team(YearDate)
        -- 7B
        ON DELETE CASCADE
        ON UPDATE RESTRICT
    
);
-- 6C no many-many relationships
-- 5D no direct supertype/subtype entities currently
