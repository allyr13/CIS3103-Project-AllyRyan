import mysql.connector
from mysql.connector import errorcode

try:
    reservationConnection = mysql.connector.connect(
        user= "root",
        password="BisonA13",
        host="127.0.0.1",
        database="RedSox"
    )
    
    

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Invalid credentials')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('Databse not found')
    else:
        print('Cannot connect to database:', err)

teamCursor = reservationConnection.cursor()


insertPlayer = ("INSERT INTO PLAYER "
                   "VALUES ('Ally', 13, 2024); ")
    
teamCursor.execute(insertPlayer)
reservationConnection.commit()
teamCursor.close()
