import json
import requests

new_data = {}
flag = False
class Main:
	try:
		with open('datainforamtion.json' , 'r') as f:
			user_inf = json.loads(f.read())
	except:
		user_inf = {}


	def __init__(self , value1 , value2 , value3 , value4 , value5):

		self.operation = value1
		self.id = value2
		self.name = value3
		self.email = value4
		self.status = value5


		self.theoperation()
		self.result()



	def theoperation(self):


		if self.operation == 'Delete':
			flag = True
			odd_data = []
			tosend = {}

			Main.user_inf.pop(str(self.id))
			flag = True
			key = str(self.id)


			for key , value in zip(Main.user_inf.keys() , Main.user_inf.values()):
				print(key)
				for item in value.values():
					odd_data += [item]

				tosend = {

					'id' : key , 
					'name' : odd_data[0] , 
					'email' : odd_data[1] , 
					'status' : odd_data[2]

				}


				requests.post(url = 'https://viciousafraidmention.watsjustice.repl.co/inf', data = tosend)

			

		if self.operation == 'Change' or  self.operation == 'Create':


			ss = {

				'id' : self.id,
				'name' : self.name,
				'email' : str(self.email) , 
				'status' : str(self.status) 
			}

			qsls = ss


			requests.post(url = 'https://viciousafraidmention.watsjustice.repl.co/inf', data = qsls)

			Main.user_inf[ss['id']] = {

				'id' : self.id,
				'name' : self.name,
				'email' : str(self.email) , 
				'status' : str(self.status) 
			}


	def result(self):
		global new_data

		new_data = Main.user_inf
	


Main('Delete' , 842 ,'TIDE' , '32131@gmail.com' , 'online')


with open('datainforamtion.json' , 'w') as f:
	json.dump(new_data, f, indent = 4 , ensure_ascii = False)