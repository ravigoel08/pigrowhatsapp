from src import app
from twilio.twiml.messaging_response import MessagingResponse
from flask import request, jsonify
import constants
from searcher import Check, Searcher

@app.route('/server',methods=['GET'])
def server():
	return 'hello'

@app.route('/incoming',methods=['POST'])
def pigro():
	msg = request.form.get('Body')
	resp = MessagingResponse()
	if(Check(msg)):
		try:
			res = Searcher(msg)
			msg = resp.message(res)
			return str(resp)
		except:
			resp.message(constants.RESULT)
			return str(resp)
	else:
		resp.message(constants.MESSAGE)
		return str(resp)
