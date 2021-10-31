import sys, os, os.path
import time

def clear():
	time.sleep(0.02)
	os.system("cls")
	pass

def profile():
	if profileFile == False:
		print("Создание профельных файлов...")
		time.sleep(0.5)
		os.system("cls")
		profileLic = open("System16\\profile.lic", 'w')
		nameProfile = str(input("Введите новое имя пользователя:\n"))
		profileWrite = profileLic.write(nameProfile)
		import subprocess
		subprocess.call(['attrib', '+h', "System16\\profile.lic"])
	else:
		pass
	return

os.system("title MinOS [Проверка]")
print("Проверка фалов, пожалуйста подождите...")
time.sleep(0.5)
sysFiles = os.path.isdir("System16")
print("Использование файлов системы: " + str(sysFiles))
time.sleep(0.5)
profileFile = os.path.isfile("System16\\profile.lic")
print("Использование файлов профиля: " + str(profileFile))
time.sleep(0.5)
clear()
os.system("title MinOS")
for i in range(101):
	print(f"{i}%")
	clear()
if sysFiles == False:
	print("Создание системных файлов...")
	time.sleep(0.5)
	os.mkdir("System16")
	import subprocess
	subprocess.call(['attrib', '+h', "System16"])
	profile()
	pass
else:
	profile()
	pass