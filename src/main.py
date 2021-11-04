import flask
import re
import random
import requests



users = {}

def check(flag):

	if flag:
		flask.session.clear() 
	else:
		pass


app = flask.Flask('my-server')

@app.route('/inf' , methods = ['GET'])
def qwe():
    return users
    
@app.route('/inf' , methods = ['POST'])
def qs():
    global users

    check(flag)


    users[flask.request.form['id']] = {

		'name' :  re.sub( '/n|1|2|3|4|5|6|7|8|9|,' , '' , str(flask.request.form['name'])) ,
		'email' : flask.request.form['email'] , 
		'status' : flask.request.form['status']

	}
    



app.run(host = '0.0.0.0' , port = 3000)
