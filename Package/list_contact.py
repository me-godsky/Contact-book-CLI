import operator
from time import gmtime, strftime
import Package.db_conn as db



def list_contacts():
	
	try :
		print()
		print('------------------ List all Contacts ------------------ \n')
		print()
		print('''         Means to list the contacts :         
  1. By Name                2. By Date and time of creation ''')
		print()
		
		x = int(input(' -> '))
		
		if x == 1 :
			conn = db.database()
			c = conn.cursor()
			c.execute('''SELECT * FROM CONTACTS ''')
			rows = c.fetchall()
			rows.sort(key = operator.itemgetter(0, 1 , 2))
			for row in rows :
				print(row)	
			print()
			print("All contacts listed successfully!")
			conn.close()
			x = False
		
		elif x == 2 :
			conn = db.database()
			c = conn.cursor()
			c.execute('''SELECT * FROM CONTACTS ''')
			rows = c.fetchall()
			rows.sort(key = operator.itemgetter(6, 7))
			for row in rows :
				print(row)	
			print()
			print("All contacts listed successfully!")
			conn.close()
			x = False

		else :
			print("Invalid input! :(")
			x = False
		

	except (KeyboardInterrupt, SystemExit):
		print()	
		print("There maybe an error while deleting contact details, try again :| ")
		return
	
	except :
		print()
		print("An unexpected error occurred while processing :(")
				
