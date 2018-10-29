import socket
import uuid, re, datetime
import urllib.request
from win32api import GetUserName
import random, time
import winshell, os

ascii = """

 _____ _                ______       _   
/  ___| |               | ___ \     | |  
\ `--.| | __ ___   _____| |_/ / ___ | |_ 
 `--. \ |/ _` \ \ / / _ \ ___ \/ _ \| __|
/\__/ / | (_| |\ V /  __/ |_/ / (_) | |_ 
\____/|_|\__,_| \_/ \___\____/ \___/ \__|


 _   _   __   _____ 
| | | | /  | |  _  |
| | | | `| | | |/' |
| | | |  | | |  /| |
\ \_/ / _| |_\ |_/ /
 \___/  \___(_)___/ 
                    


"""

print (ascii)
print ("\n")

Master = "c0d3ninja"
AI_NAME = "Ex Machina"

def say():
	random_words = ["Don't leave this blank", "What can I do for you?",
	"Anything that you need?", "Say something!!"]
	return random.choice(random_words)

def deleteafile():
	try:
		file = input("Location?: ")
		file = str(file)
		print ("Deleting file: " + file + "\n")
		print ("please wait ....." + "\n")
		time.sleep(3)
		os.remove(file)
		print ("File has been deleted!" + "\n")
	except WindowsError:
		print ("Couldn't find the file, Try again please")

def recyclebin():
	print ("Emptying the Recycle Bin, please wait..")
	time.sleep(3)
	return winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)

def localip():
	try:
		hostname = socket.gethostname()
		IP = socket.gethostbyname(hostname)
		return "Your local IP is: " + IP
	except socket.error:
		print ("Coulnd't retrieve your IP")

def externalip():
	ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
	return "Your external IP is: " + ip

def mac():
	return ':'.join(re.findall('..', '%012x' % uuid.getnode()))

def currentime():
	Daytime = datetime.datetime.now()
	return Daytime.strftime("%a, %b %d, %Y")

def username():
	user = GetUserName()
	return "Your Username is: " + user

print ("WELCOME " + Master + "\n")
print (AI_NAME + " is now loading......." + "\n")
time.sleep(3)

while True:
	prompt = input("Yes Master?: ")
	if "What is my ip?" in prompt:
		print (localip())
		print (externalip())
	elif "Delete a file" in prompt:
		print (deleteafile())
	elif "Empty the recycle bin" in prompt:
		print (recyclebin())
	elif prompt == "":
		print (say())
	elif "mac?" in prompt:
		print (mac())
	elif "What is your name?" in prompt:
		print (AI_NAME)
	elif "Who is your master?" in prompt:
		print ("My masters name is c0d3ninja!!")
	elif "Datetime?" in prompt:
		print (currentime())
	elif "username?" in prompt:
		print (username())
	elif "shutdown!" in prompt:
		print ("Shutting down now " + Master)
		exit()
