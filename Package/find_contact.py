import Package.db_conn as db


def find_contact():
	try :
		print()
		print('------------------ Search Contact Details ------------------ \n')
		print()
		print('''         Means to search the contact details :         
  1. By Name                2. By First name and Number ''')
		print()
		
		x = int(input(' -> '))

		while x :
			if x == 1 :
				print()
				f = str(input(' -> First Name : '))
				m = str(input(' -> Middle Name : '))
				l = str(input(' -> Last Name : '))
				conn = db.database()
				c = conn.cursor()
				c.execute('''SELECT * FROM CONTACTS WHERE FIRST_NAME = ? AND MIDDLE_NAME = ? AND LAST_NAME = ? ''', (f , m , l))
				print(c.fetchall())				
				print()
				conn.close()
	
			elif x == 2 :
				print()
				f = str(input(' -> First Name : '))
				n = int(input(' -> Number : '))
				conn = db.database()
				c = conn.cursor()
				c.execute('''SELECT * FROM CONTACTS WHERE FIRST_NAME = ? AND NUMBER = ?''', (f , n))
				print(c.fetchall())
				print()
				conn.close()
	
			else :
				print("Invalid input! :(")


			a = str(input('Do you want to find details of another contact[ y or n ] : '))
			
			if a == 'y' or a == 'Y' :
				find_contact()
				
			elif a == 'n' or a == 'N' :
				x = False
				print("Ohkk, tata ;) ")
				break
			else :
				print(" Enter y or n")
				continue
			
			break

	except (KeyboardInterrupt, SystemExit):
		print()	
		print("There maybe an error while finding contact details, try again :| ")
		return
	
	except :
		print()
		print("An unexpected error occurred while processing :(")

		

