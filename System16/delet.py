import os
import time

def clear():
	time.sleep(1)
	os.system("cls")
	pass

def menu():
	clear()
	print("Введите какой тип вы хотите удалить>> ")
	print("folder - папка")
	print("file - файл")

menu()

while True:
	command = input("Введите что вы хотите удалить(menu вернуться в меню)>> ")
	if command == str("folder"):
		name = input("Название папки>> ")
		os.rmdir(name)
		print("Папка удалена")
		menu()
	elif command == str("file"):
		name = input("Название файла с разрешением(.txt, .py, .java)>> ")
		os.remove(name)
		print("Файл удалён")
		menu()
	elif command == str("menu"):
		clear()
		os.system("python MinOS.py")
	else:
		print("Ошибка написания!")
		clear()
		menu()