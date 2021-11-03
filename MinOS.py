import os
import time

def clear():
	time.sleep(1)
	os.system("cls")
	pass

def cd(folder):
	os.chdir(folder)

def help():
	clear()
	print("######################################")
	print("Все команды")
	print("exit - выйти из ос")
	print("menu - выйти в меню")
	print("######################################")
	print("math - открыть калькулятор")
	print("######################################")
	print("create - создать что-то")
	print("delet - удалить что-то")
	print("ls - вывести содержимое папки")
	print("rename - переминовать что-то")
	print("######################################")
	print("edit - редактирование файлов")
	print("######################################")
	print("cd - переключение между папками")
	print("######################################")

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
		print("Starting Math...")
		time.sleep(0.2)
		os.chdir("System16")
		os.system("math.bat")
		os.system("cls")
		os.chdir("..")
		menu()
	elif command == str("cd"):
		folder = input("Введите название папки>> ")
		if folder != "..":
			cd(folder)
		else:
			cd("..")
		menu()
	elif command == str("create"):
		menu()
		command = input("folder\nfile\nВведите что вы хотите создать(menu вернуться в меню)>> ")
		if command == str("folder"):
			name = input("Название папки>> ")
			os.mkdir(name)
			print("Папка создана")
		elif command == str("file"):
			name = input("Название файла с разрешением(.txt, .py, .java)>> ")
			file = open(name, "w")
			print("Файл создан")
			menu()
	elif command == str("delet"):
		menu()
		command = input("folder\nfile\nВведите что вы хотите удалить(menu вернуться в меню)>> ")
		if command == str("folder"):
			name = input("Название папки>> ")
			os.rmdir(name)
			print("Папка удалена")
		elif command == str("file"):
			name = input("Название файла с разрешением(.txt, .py, .java)>> ")
			os.remove(name)
			print("Файл удалён")
			menu()
		elif command == str("System16"):
			print("Данная папка евляется системной!\nеё невозможно удалить")
	elif command == str("ls"):
		print(os.listdir())
	elif command == str("rename"):
		menu()
		name = input("folder\nfile\nВыберите что вы хотите переминовать(menu вернуться в меню)>> ")
		if name == str("folder"):
			foldername = input("Введите название папки>> ")
			newfoldername = input("Введите новое имя папки>> ")
			os.rename(foldername, newfoldername)
			print("Папка переминована")
		elif name == str("file"):
			filename = input("Введите название файла>> ")
			newfilename = input("Введите новёе название файла>> ")
			os.rename(filename, newfilename)
	elif command == str("edit"):
		file = input("Введите название файла(test.txt, test.py, test.java)>> ")
		myfile = open(file, "r")
		dan = myfile.readline()
		print(dan)
		try:
			myfile = open(file, "a")
			text = input("Введите текст(menu)>>")
			if text == str("menu"):
				menu()
			else:
				myfile.writelines(text)[1]
		except Exception as e:
			myfile.close()
		finally:
			myfile.close()
			menu()
	else:
		print("Комманда не была обнаружена")
		menu()