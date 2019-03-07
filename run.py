import os
os.system("clear")
print("""\033[5;34;40m\n
 ____  ____                 _   _   _             _
|  _ \|  _ \  ___  ___     / \ | |_| |_ __ _  ___| | __
| | | | | | |/ _ \/ __|   / _ \| __| __/ _` |/ __| |/ /
| |_| | |_| | (_) \__ \  / ___ \ |_| || (_| | (__|   <
|____/|____/ \___/|___/ /_/   \_\__|\__\__,_|\___|_|\_\
""")  
os.system("chmod +x xerxes.c")
a = input("\033[5;32;40m\n Enter website address eg : www.fakesite.com \n Website Name : ")
os.system("./xerxes "+a+" 80")
