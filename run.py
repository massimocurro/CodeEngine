#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import os
import pip._vendor.requests
import json
from flask import Flask

app = Flask(__name__)


@app.route("/")
def createF():
    headers = {"Content-Type": "application/json"}
    response = pip._vendor.requests.get('https://function-76.1at6rgz00yjr.eu-de.codeengine.appdomain.cloud')
    return {'message': response.text}
