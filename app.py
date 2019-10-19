from flask import Flask,Response
from flask_restful import Resource,Api
from twilio.twiml.messaging_response import MessagingResponse
from flask import request, jsonify
from twilio.rest import Client
import requests
app = Flask(__name__)
#api = Api(app)
#client = Client(account_sid,auth_token)
#class pigro(Resource):
#	def post(self):
#		msg =  request.form.get('Body')
#		req = requests.get(f'https://api.duckduckgo.com/?skip_disambig=1&
#format=json&pretty=1&q={msg}').json()
#		heading = req['Heading']
#		ab_text = req['AbstractText']
#		if ab_text == "":
#			ab_text = req['RelatedTopics'][0]['Text']
#		mes = heading +'\n\n'+ab_text
#		resp = MessagingResponse()
#		resp.message(f"Answer : {mes}")
#		print(resp)
#		return str(resp)
#api.add_resource(pigro,'/incoming')
@app.route('/server',method=['GET'])
def server():
	return 'hello'
@app.route('/incoming',methods=['POST'])
def pigro():
	msg = request.form.get('Body')
	print(msg)
	if(msg.lower().strip()!="hi" and msg.lower().strip()!="hello" and msg.lower().strip()!="help" and msg.lower().strip()!="about" and msg.lower().strip()!="pigro" and msg.lower().strip()!="pigrobot"):
		try:
			req = requests.get(f'https://api.duckduckgo.com/?skip_disambig=1&format=json&pretty=1&q={msg}').json()
			heading = req['Heading']
			ab_text = req['AbstractText']
			if ab_text == "":
				ab_text = req['RelatedTopics'][0]['Text']
			mes = heading +'\n\n'+ab_text
			resp = MessagingResponse()
			resp.message(f"{mes}")
			return str(resp)
		except:
			resp = MessagingResponse()
			resp.message('Result not found!')
			return str(resp)
	else:
		resp = MessagingResponse()
		resp.message('I am PigroBot which help you to get quick information from WikiPedia pages, right within WhatsApp.\nTry me, send me anything you want information about. \n I am Developed by Ravi Goyal. Follow him https://www.instagram.com/sypherrv/ ')
		return str(resp)
if __name__=='__main__':
	app.run(threaded=True, port=5000)
