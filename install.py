import msvcrt
import os
import shutil
import requests


def getch(text, answer):
	print("*{1}* {0} ".format(text, answer), end="")
	key = msvcrt.getch().decode()
	print(key)
	return key


def getdir(path):
	download = {}
	response = requests.get(path)

	for resource in response.json():
		if resource["path"] in EXCEP:
			continue

		if resource["type"] == "dir":
			download.update(getdir(resource["url"]))
		else:
			content = requests.get(resource["download_url"]).text
			download.update({resource["path"]: content})

	return download


def install(path):
	print("Downloading...")
	download = getdir(REPO_URL)

	print("Installing...")
	for name in download.keys():
		file_path = os.path.join(path, name)
		os.makedirs(os.path.dirname(file_path), exist_ok=True)

		file = open(file_path, "w")
		file.write(download[name])
		file.close()

	print()
	print("Installation complete!")

	sure = getch("Startup MinOS?", "Y/N")
	if sure == "Y":
		os.system(os.path.join(path, "start.bat"))


REPO_URL = "https://api.github.com/repos/Gitsans66/MinOS/contents"
EXCEP = [".gitignore", "install.py"]

print("MinOS Installer")
print()

while True:
	disk = getch("Select disk:", "DISK CHAR").upper() + ":"
	if os.path.exists(disk):
		print("Installer create folder on this path: " + disk + "\MinOS")
		sure = getch("Did you sure?", "Y/N").upper()

		print()
		if sure == "Y":
			path = os.path.join(disk + "\MinOS")
			if os.path.exists(path):
				print(path + " already exists...")
				print("Installer will remove folder contents")
				sure = getch("Continue?", "Y/N").upper()

				print()
				if sure == "Y":
					shutil.rmtree(path)
					break
			else:
				break

	else:
		print("This disk does not exist...")
		print()

os.mkdir(path)
install(path)
