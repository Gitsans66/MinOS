import os
import time

def clear():
	time.sleep(1)
	os.system("cls")
	pass

def menu():
	clear()
	print("Выберите что вы хотите создать.")
	print("folder - папка")
	print("file - файл")

menu()

while True:
	command = input("Введите что вы хотите создать(menu вернуться в меню)>> ")
	if command == str("folder"):
		name = input("Название папки>> ")
		os.mkdir(name)
		menu()
	elif command == str("file"):
		name = input("Название файла с разрешением(.txt, .py, .java)>> ")
		file = open(name, "w")
		print("Файл создан")
		menu()
	elif command == str("menu"):
		clear()
		os.system("python MinOS.py")
	else:
		print("Ошибка написания!")
		clear()
		menu()