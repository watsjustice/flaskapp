import random
import requests
import json
import re



from bs4 import BeautifulSoup as bs


r = requests.get(url = 'https://www.ssa.gov/oact/babynames/decades/century.html').text
q = bs(r , 'lxml').find('tbody').find_all('tr')

names = []


for item in q:
    try:

        names += [re.sub( '/n|1|2|3|4|5|6|7|8|9|,' , '' , str(item.find('td').find_next_sibling().text))]
    except:
        pass


for item in q:

    names += [str(item.text)]


data_saver = {}
for i in range(10): #для изменения кол-ва пользователей


	try:

		a = list('qwertyuiopasdfghjklzxcvbnm')
		random.shuffle(a)

		data1 = {

			'id' :  random.choice(list(range(10000))),

			'name' : names[random.randint(1 , 30)] ,

			'email' : ''.join([x for x , y  in zip( a , range(5))]) + '@gmail.com' , 

			'status' : random.choice(['online' , 'offline'])


		}

		data_saver[data1['id']] = {

			'name' : data1['name'] ,

			'email' : data1['email'], 

			'status' : data1['status']
		} 

		with open('datainforamtion.json', 'w') as f:
			json.dump(data_saver , f  , indent = 4 , ensure_ascii = True)

		requests.post(url = 'https://viciousafraidmention.watsjustice.repl.co/inf', data = data1)



	except Exception as ex:
		print(ex)
		break




	
	







	
	


