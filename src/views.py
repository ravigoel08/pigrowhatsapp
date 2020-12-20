from src import app
from twilio.twiml.messaging_response import MessagingResponse
from flask import request, jsonify, Blueprint
import requests
import constants
from searcher import Check, Searcher

views = Blueprint("views", __name__)


@views.route("/incoming", methods=["POST"])
def pigro():
    msg = request.form.get("Body")
    resp = MessagingResponse()
    if Check(msg):
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
