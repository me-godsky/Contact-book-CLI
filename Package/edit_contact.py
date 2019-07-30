from time import gmtime, strftime
import Package.db_conn as db

def edit_contact():
	
	try :
		print()
		print('------------------ Edit Contact ------------------ ')
		print()
		print('''			   **** WARNING **** 
If you do not enter the correct first, middle, last names correctly, the data won't be updated
''')
		f = str(input(' -> First Name : '))
		m = str(input(' -> Middle Name : '))
		l = str(input(' -> Last Name : '))
		print('''Which detail you want to change :
  1. First Name
  2. Middle Name
  3. Last Name
  4. Number
  5. Address
  6. Email
''')
		x = int(input())
		
		while x :

			if x == 1 :
				y = str(input("Enter new First Name : "))
				if len(y) < 3:
					print('Length of first name should be greater than 2')
					pass

				conn = db.database()
				conn.execute('''UPDATE CONTACTS SET FIRST_NAME = ? WHERE FIRST_NAME= ? AND MIDDLE_NAME = ? AND LAST_NAME = ?''', (y, f, m ,l))
				conn.commit()
				print("Contact Detail Updated successfully")
				conn.close()

			elif x == 2 :
				y = str(input("Enter new Middle Name : "))
				conn = db.database()
				conn.execute('''UPDATE CONTACTS SET MIDDLE_NAME = ? WHERE FIRST_NAME= ? AND MIDDLE_NAME = ? AND LAST_NAME = ?''', (y, f, m ,l))
				conn.commit()
				print("Contact Detail Updated successfully")
				conn.close()
								
			elif x == 3 :
				y = str(input("Enter new Last Name : "))
				if len(y) < 3:
					print('Length of last name should be greater than 2')
					pass


				conn = db.database()
				conn.execute('''UPDATE CONTACTS SET LAST_NAME = ? WHERE FIRST_NAME= ? AND MIDDLE_NAME = ? AND LAST_NAME = ?''', (y, f, m ,l))
				conn.commit()
				print("Contact Detail Updated successfully")
				conn.close()
							
			elif x == 4 :
				number = int(input("Enter new Number : "))
				if number :
					c = str(number)
					if len(number) < 10:
						print('Number should be exactly of 10 digits')
						pass
		
					elif not c[0] == '9' or c[0] == '8' or c[0] == '7' :
						print('Number must start with 9,8,7 ')
						pass
					
					elif len(number) > 10 :
						print('Length of number greater than 10')
						pass		
					else :
						continue		

				conn = db.database()
				conn.execute('''UPDATE CONTACTS SET NUMBER = ? WHERE FIRST_NAME= ? AND MIDDLE_NAME = ? AND LAST_NAME = ?''', (number, f, m ,l))
				conn.commit()
				print("Contact Detail Updated successfully")
				conn.close()
			
			elif x == 5 :
				y = str(input("Enter new Address : "))
				conn = db.database()
				conn.execute('''UPDATE CONTACTS SET ADDRESS = ? WHERE FIRST_NAME= ? AND MIDDLE_NAME = ? AND LAST_NAME = ?''', (y, f, m ,l))
				conn.commit()
				print("Contact Detail Updated successfully")
				conn.close()
			
			elif x == 6 :
				email = str(input("Enter new Email : "))
				if email :
					s_prcocess = email.replace('@','.').split('.')
					order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468-_'
					if len(email) < 3:
						print('Length of email should be greater than 2')
						pass
				
					elif all(s_items != '' for s_items in s_prcocess):
						if not len(s_prcocess[2]) <= 3 and s_prcocess[1].isalnum() and all(item in order for item in s_prcocess[0]):
							print('Improper context of email')
							pass
			
				conn = db.database()
				conn.execute('''UPDATE CONTACTS SET EMAIL = ? WHERE FIRST_NAME= ? AND MIDDLE_NAME = ? AND LAST_NAME = ?''', (email, f, m ,l))
				conn.commit()
				print("Contact Detail Updated successfully")
				conn.close()						

			else :
				print("Invalid Option! :( ")


				
			a = str(input('Do you want to continue editing this contact [ y or n ] : '))
			
			if a == 'y' or a == 'Y' :
				x = int(input('''Enter the option to be updated : 
  1. First Name  2. Middle Name   3. Last Name
  4. Number      5. Address       6. Email 
'''))
			elif a == 'n' or a == 'N' :
				x = False
				print("Ohkk, tata ;) ")
			
			else :
				print(" Enter y or n")
				continue
		
		b = str(input('Do you want to update date and time of creation of this contact as well? [y or n] : '))
		print()
		
		if b == 'y' or b == 'Y' :
			c = strftime("%Y-%m-%d", gmtime())                                                                 
			d = strftime("%H:%M:%S", gmtime())
			conn.execute('''UPDATE CONTACTS SET DATE = ? AND TIME = ? WHERE FIRST_NAME= ? AND MIDDLE_NAME = ? AND LAST_NAME = ?''', (c , d , f, m ,l))
			conn.commit()
			print("Contact Detail Updated successfully")
			conn.close()

		elif b == 'n' or b == 'N' :
			print('Ohkk sir :) ')
		
		else :
			print('Invalid input :( ')
		

	except (KeyboardInterrupt, SystemExit):	
		print("There maybe an error while adding contact details, try again :| ")
		return
	
	except :
		raise		
	
