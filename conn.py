import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('''CREATE TABLE CONTACTS
        (FIRST_NAME           TEXT 	PRIMARY KEY    NOT NULL,
	 MIDDLE_NAME           TEXT 	NOT NULL, 
	 LAST_NAME           TEXT 	NOT NULL,
         NUMBER            INT     NOT NULL,
         ADDRESS        CHAR(50),
         EMAIL         CHAR(50),
	 DATE		TEXT,
	 TIME		TEXT);''')
print("Database created successfully!")
		

