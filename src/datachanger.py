import json
import requests

new_data = {}

class Main:
	try:
		with open('datainforamtion.json' , 'r') as f:
			user_inf = json.loads(f.read())
	except:
		user_inf = {}
	

	titles = [f'value_{item}' for item in ['type' , 'id' , 'name' , 'email' , 'status']]
		

	def __init__(self , *kwargs):


		globals().update({item : object for item , object in zip(Main.titles , kwargs)})

		self.operation = value_type
		self.id = value_id
		self.name = value_name
		self.email = value_id
		self.status = value_status

		self.theoperation()
		self.result()




	def theoperation(self):


		if self.operation == 'Delete':

			requests.post(url = 'https://viciousafraidmention.watsjustice.repl.co/inf', data = { 'Access' : 'Allowed'})

			odd_data = []
			tosend = {}

			Main.user_inf.pop(str(self.id))
			key1 = str(self.id)


			for key , value in zip(Main.user_inf.keys() , Main.user_inf.values()):
				for item in value.values():
					odd_data += [item]

				tosend = {
					'Access' : 'Delete' ,
					'id' : key , 
					'name' : odd_data[0] , 
					'email' : odd_data[1] , 
					'status' : odd_data[2]

					}
				odd_data = []




				requests.post(url = 'https://viciousafraidmention.watsjustice.repl.co/inf', data = tosend)


			

		if self.operation == 'Change' or  self.operation == 'Create':


			Main.user_inf[self.id] = {
				'Access' : 'Create/Change' , 
				'id' : self.id , 
				'name' : self.name,
				'email' : str(self.email) , 
				'status' : str(self.status) 
			}

			requests.post(url = 'https://viciousafraidmention.watsjustice.repl.co/inf', data = Main.user_inf[self.id] )


	def result(self):
		global new_data
		new_data = Main.user_inf
		return print(f'The operation {self.operation} has been successful done')

	def __str__(self):
		return print(f'The operation {self.operation} has been successful done')
	

titles = ['type ', 'id ' , 'name ' , 'email ' , 'status ']
value1 = []
for iteri in range(5):
	value1 += [input(f'{titles[iteri]}')]

Main(*value1)



with open('datainforamtion.json' , 'w') as f:
	json.dump(new_data, f, indent = 4 , ensure_ascii = False)
