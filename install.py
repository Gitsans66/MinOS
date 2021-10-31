import os
import msvcrt
from os import path
import requests

def ginput(text):
    print(text, end="")
    key = msvcrt.getch().decode()
    print(key)
    return key

print("MinOS Installer")
print()

while True:
    disk = ginput("*DISK CHAR* Select disk: ").upper() + ":"
    if path.exists(disk):
        print("Installer create folder on this path: " + disk + "\MinOS")
        print
        sure = ginput("*Y/N* Did you sure? ").upper()

        if sure == "Y":
            break
        else:
            print()
    else:
        print("This disk does not exist...")
        print()

# TODO - create folder
# TODO - clone repo