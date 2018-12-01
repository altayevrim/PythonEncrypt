import os
import sys
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
KEYFILE = "rimtay.key"
RUN = True
def decrypt(filename):
	if(os.path.exists(filename) == True):
		new_name = filename.rstrip("_rimenc")
		os.rename(filename,new_name)
		file = open(new_name,"rb+")
		data = file.read()
		file.close()
		# file.close()
		if(len(data) > 0):
			fernet = Fernet(key)
			try :
				decrypted = fernet.decrypt(data)
			except InvalidToken:
				print("FAILED '"+filename +"' could not decrypted because key invalid")
				os.rename(new_name,filename)
			except TypeError:
				print("FAILED '"+filename +"' could not decrypted because the data is not binary")
				os.rename(new_name,filename)
			else :
				file = open(new_name,"wb")
				change = file.write(decrypted)
				file.close()
				print("SUCCESS '"+filename +"' has decrypted and renamed as '"+new_name+"'")
		else :
			print("WARNING '"+filename +"' could not decrypted because it's empty")
		

if os.path.exists(KEYFILE) == False : 
	print("Encryption Key is not found! System will not work!")
	RUN = False
else:
	file = open(KEYFILE, "rb")
	key = file.read()
	print("Encryption Key File found on the system.")
	file.close()
if(RUN):
	print("Encryption Key: " + str(key))

	for root, dirs, files in os.walk(".") :
		for filename in files:
			# name,extension = os.path.splitext(filename)
			# extension = extension.lower()
			parts = filename.split("_")
			
			if(parts[-1] == "rimenc"):
				decrypt(filename)
				# print(filename)
	print("\n\nPress enter to exit!")			
	wait = input()