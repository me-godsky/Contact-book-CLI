from time import gmtime, strftime
import Package.db_conn as db

def add_contact():

	try :
		print("----------- Fill the details of the new contact : ----------- ")
		print()
		first_name = str(input(' -> First Name : '))
		middle_name = str(input(' -> Middle Name : '))
		last_name = str(input(' -> Last Name : '))
		number = str(input(' -> Mobile Number : '))
		address = str(input(' -> Address : '))
		email = str(input(' -> Email : '))
		date = strftime("%Y-%m-%d", gmtime())                                                                 
		time = strftime("%H:%M:%S", gmtime())                                                                                         	
		conn = db.database()
		
		if len(first_name) < 3:
			print('Length of first name should be greater than 2')
			d = True
		
		else :
			d = False
		
		if len(last_name) < 3:
			print('Length of last name should be greater than 2')
			d = True

		else :
			d = False

		if number :
			c = str(number)
			if len(number) < 10:
				print('Number should be exactly of 10 digits')
				d = True

			elif not c[0] == '9' or c[0] == '8' or c[0] == '7' :
				print('Number must start start with 9,8,7 ')
				d = True
			
			elif len(number)> 10 :
				print('Length of number greater than 10')
				d = True

			else :
				d = False			

		if email :
			s_prcocess = email.replace('@','.').split('.')
			order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468-_'
			if len(email) < 3:
				print('Length of email should be greater than 2')
				d = True
			
			elif all(s_items != '' for s_items in s_prcocess):
				if not len(s_prcocess[2]) <= 3 and s_prcocess[1].isalnum() and all(item in order for item in s_prcocess[0]):
					print('Improper context of email')
					d = True

			else :
				d = False

	
		if d :
			return

		conn.execute('''INSERT INTO CONTACTS ( FIRST_NAME , MIDDLE_NAME , LAST_NAME , NUMBER , ADDRESS , EMAIL , DATE , TIME) \
      		VALUES(?,?,?,?,?,?,?,?)''', (first_name, middle_name, last_name, number, address, email , date , time));
		conn.commit()
		print(" Contact saved successfully! :) ")
		conn.close()		

	
	except (KeyboardInterrupt, SystemExit):	
		print("There was an error while adding contact details, try again :| ")
		return
	
	except :
		raise
			

