import flask
import re
import requests
from flask_login import logout_user

users = {}
app = flask.Flask('my-server')



@app.route('/inf' , methods = ['GET'])
def qwe():
	return users




@app.route('/inf' , methods = ['POST'])
def qs():
	global users

	try:
		if flask.request.form['Access'] == 'Allowed':
			users = {}
	except:
		pass

	users[flask.request.form['id']] = {
			'name' :  re.sub( '/n|1|2|3|4|5|6|7|8|9|,' , '' , str(flask.request.form['name'])) ,
			'email' : flask.request.form['email'] , 
			'status' : flask.request.form['status']
			}
			
	return users



app.run(host = '0.0.0.0' , port = 3000)
