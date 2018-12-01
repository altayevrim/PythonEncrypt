import os
import sys
from cryptography.fernet import Fernet
KEYFILE = "rimtay.key"
RUN = True
def decrypt(filename):
	if(os.path.exists(filename) == True):
		os.rename(filename,filename.rstrip("_rimenc"))
		new_name = filename.rstrip("_rimenc")
		file = open(new_name,"rb+")
		data = file.read()
		file.close()
		# file.close()
		if(len(data) > 0):
			fernet = Fernet(key)
			decrypted = fernet.decrypt(data)
			
			file = open(new_name,"wb")
			change = file.write(decrypted)
			# print(encrypted)
			
			print("'"+filename +"' has decrypted and renamed as '"+new_name+"'")
		else :
			print("'"+filename +"' could not decrypted because it's empty")
		file.close()

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