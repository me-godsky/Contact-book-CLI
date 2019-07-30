import Package.db_conn as db
import shutil, os

def download_contact():
	try :
		conn = db.database()
		c = conn.cursor()
		file1 = str(input('Enter name of file to in which contacts are to be exported! : '))
		file1 = file1 + '.txt'
		path = os.getcwd() 
		os.chdir(path + '/Exported_Contact_files/')
		myfile = open(file1,'w')
		myfile.write('FIRST_NAME'.rjust(0))
		myfile.write('MIDDLE_NAME'.rjust(20))
		myfile.write('LAST_NAME'.rjust(20))
		myfile.write('NUMBER'.rjust(20))
		myfile.write('ADDRESS'.rjust(20))
		myfile.write('EMAIL'.rjust(20))
		myfile.write('DATE'.rjust(20))
		myfile.write('TIME'.rjust(20))
		myfile.writelines('') 
		myfile.write("\n")
		x = c.execute('''SELECT * FROM CONTACTS ''' )
		for row in x:
			myfile.write("\n")
			for i in range(len(row)) :
				if len(str(row[i]))< 21 :
					myfile.write((str(row[i]) + ' '*(21 - len(str(row[i])))))
				else :
					myfile.write((str(row[i])))
			myfile.write("\n")
		conn.commit()
		myfile.close()
		os.chdir(path)
		print("Contacts exported to %s successfully! " % (file))		
		print("You can find your exported file in 'Exported_Contact_files' folder :)")
		

	except (KeyboardInterrupt, SystemExit):
		print()	
		print("There maybe an error while finding contact details, try again :| ")
		return
	
	except :
		print()
		print("An unexpected error occurred while processing :(")


