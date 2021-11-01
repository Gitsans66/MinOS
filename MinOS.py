import os
import time

def clear():
	time.sleep(1)
	os.system("cls")
	pass

def help():
	clear()
	print("################################")
	print("Все команды")
	print("exit - выйти из ос")
	print("menu - выйти в меню")
	print("################################")
	print("math - открыть калькулятор")
	print("################################")
	print("create - создать что-то")
	print("delet - удалить что-то")
	print("ls - вывести содержимое папки")
	print("################################")

def menu():
	clear()
	print("############################")
	print('Добро пожаловать, %s!' % str(name))
	print('Мы приветствуем вас в MinOS!')
	print("############################")

os.system("python MinCore.py")
os.system("title MinOS [Запуск]")
clear()
nameProfile = open("System16\\profile.lic", 'r+', encoding="utf-8")
name = nameProfile.read()
os.system("title MinOS")
menu()
while True:
	print("Введите команду>>")
	command = input();
	if command == str("help"):
		help()
	elif command == str("exit"):
		print("Завершение работы")
		clear()
		break;
	elif command == str("menu"):
		menu()
	elif command == str("math"):
		print("Starting mMath...")
		time.sleep(0.2)
		os.chdir("System16")
		os.system("math.bat")
		os.system("cls")
		os.chdir("..")
		menu()
	elif command == str("create"):
		os.system("python System16/create.py")
	elif command == str("delet"):
		os.system("python System16/delet.py")
	elif command == str("ls"):
		print(os.listdir())
	
	else:
		print("Комманда не была обнаружена")
		menu()