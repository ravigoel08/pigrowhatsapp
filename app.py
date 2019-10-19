from flask import Flask,Response
from flask_restful import Resource,Api
from twilio.twiml.messaging_response import MessagingResponse
from flask import request, jsonify
from twilio.rest import Client
import requests
app = Flask(__name__)
@app.route('/server',methods=['GET'])
def server():
	return 'hello'
@app.route('/incoming',methods=['POST'])
def pigro():
	msg = request.form.get('Body')
	resp = MessagingResponse()
	if(msg.lower().strip()!="hi" and msg.lower().strip()!="hello" and msg.lower().strip()!="help" and msg.lower().strip()!="about" and msg.lower().strip()!="pigro" and msg.lower().strip()!="pigrobot"):
		try:
			req = requests.get(f'https://api.duckduckgo.com/?skip_disambig=1&format=json&pretty=1&q={msg}').json()
			heading = req['Heading']
			ab_text = req['AbstractText']
			if ab_text == "":
				ab_text = req['RelatedTopics'][0]['Text']
			#mes = heading+'\n\n'+ab_text
			msg = resp.message('*'+req["Heading"]+'*'+req["ab_text"])
			return str(resp)
		except:
			resp.message('_Result not found!_')
			return str(resp)
	else:
		resp.message('Hey 👋 I am *PigroBot* which help you to get quick information from WikiPedia pages, right within WhatsApp.\nTry me, send me anything you want information about. \n I am Developed by *Ravi Goyal*. Follow him 💚  https://www.instagram.com/sypherrv/ and https://github.com/ravigoel08/')
		return str(resp)
if __name__=='__main__':
	app.run(threaded=True, port=5000)
