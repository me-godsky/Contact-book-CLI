from Package import add_contact as ad
from Package import edit_contact as ed
from Package import delete_contact as d
from Package import list_contact as l
from Package import find_contact as f
from Package import export_contact as ex
from Package import about as ab
from Package import banner as ba
from Package import db_conn as co

import sqlite3
import os
import shutil
import operator

def main():
	x = 1
	ba.banner()
	try :
		while x :
			i = int(input('''

  1. Add Contact
  2. Edit Contact
  3. Delete Contact
  4. List Contacts
  5. Find Contact Details
  6. Download Contact Details
  7. About

-> What do you want me to do? : '''))


			options = {

			0 : ad.add_contact,
			1 : ed.edit_contact,
			2 : d.delete_contact,
			3 : l.list_contacts,
			4 : f.find_contact,
			5 : ex.download_contact,
			6 : ab.about

			}
			
			if i == 1 :
				options[i-1]()
			
			elif i == 2 :
				options[i-1]()

			elif i ==3 :
				options[i-1]()

			elif i == 4 :
				options[i-1]()

			elif i == 5 :
				options[i-1]()

			elif i == 6 :
				options[i-1]()

			elif i ==7 :
				options[i-1]()

			else :
				print("Invalid input! ")

			x= str(input("Do you want to continue ! [y or n]  :   "))
						
			if x == 'y' or x == 'Y':
				continue
			
			elif x == 'n' or x == 'N':
				x = False

			else :
				print(" wrong context, exiting :( ")
				x = False

	except KeyError:
		process_default()

	finally :
						print('''

		SAYONARA , SEE YA SOON ;)
			
''')

			
def process_default():
	print(" Invalid argument or an error occured while processing! ")

if __name__ == "__main__" :
	main()





