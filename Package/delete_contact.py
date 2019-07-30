from time import gmtime, strftime
import Package.db_conn as db


def delete_contact():
	
	try :
		print()
		print('------------------ Delete Contact ------------------ \n')
		print()
		print('''         Means to delete the contact :         
  1. By Name                2. By First name and Number ''')
		print()
		
		x = int(input(' -> '))

		while x :
			if x == 1 :
				print()
				print('''   			   **** WARNING **** 
If you do not enter the correct first, middle, last names correctly, the contact won't be deleted
''')
				print()
				f = str(input(' -> First Name : '))
				m = str(input(' -> Middle Name : '))
				l = str(input(' -> Last Name : '))
				conn = db.database()
				conn.execute('''DELETE FROM CONTACTS WHERE FIRST_NAME = ? AND MIDDLE_NAME = ? AND LAST_NAME = ? ''', (f , m , l))
				conn.commit()
				print()
				print("Contact deleted successfully!")
				conn.close()
	
			elif x == 2 :
				print('''      			   **** WARNING **** 
If you do not enter the correct first name and number correctly, the contact won't be deleted
''')
				f = str(input(' First Name : '))
				n = int(input(' -> Number : '))
				conn = db.database()
				conn.execute('''DELETE FROM CONTACTS WHERE FIRST_NAME = ? AND NUMBER = ?''', (f , n))
				conn.commit()
				print()
				print("Contact deleted successfully!")
				conn.close()
	
			else :
				print("Invalid input! :(")


			a = str(input('Do you want to delete another contact[ y or n ] : '))
			
			if a == 'y' or a == 'Y' :
				delete_contact()

			elif a == 'n' or a == 'N' :
				x = False
				print("Ohkk, tata ;) ")
				break
			else :
				print(" Enter y or n")
				continue
		

	except (KeyboardInterrupt, SystemExit):
		print()	
		print("There maybe an error while deleting contact details, try again :| ")
		return
	
	except :
		print()
		print("An unexpected error occurred while processing :(")

