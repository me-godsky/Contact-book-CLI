import sqlite3
import shutil, os

def database():

	try :
		conn = sqlite3.connect('database.db')
		return conn
	
	except sqlite3.Error:
		print(" Warning no previous database file found, creating a new one!")
		conn = sqlite3.connect('database.db')
		conn.execute('''CREATE TABLE CONTACTS
        (FIRST_NAME           TEXT 	PRIMARY KEY    NOT NULL,
	 MIDDLE_NAME           TEXT, 
	 LAST_NAME           TEXT 	NOT NULL,
         NUMBER            INT     NOT NULL,
         ADDRESS        CHAR(50),
         EMAIL         CHAR(50),
	 DATE		TEXT,
	 TIME		TEXT);''')

		print("Database created successfully!")
		shutil.move(database.db, '/home/godsky/Desktop/ContactBook/Package/db_conn')		
		return conn	
