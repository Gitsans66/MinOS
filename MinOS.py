import os
import time

def clear():
	time.sleep(1)
	os.system("cls")
	pass

def help():
	print("################################")
	print("Все команды")
	print("exit - выйти из ос")
	print("menu - выйти в меню")
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
	if command == "help":
		clear()
		help()
	elif command == "exit":
		print("Завершение работы")
		clear()
		break;
	elif command == "menu":
		menu()
	else:
		print("Комманда не была обнаружена")
		menu()