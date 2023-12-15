import sys
import json
import pip._vendor.requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main(dict):
    response = pip._vendor.requests.get('https://function-76.1at6rgz00yjr.eude.codeengine.appdomain.cloud')
    return {'message': response.text}
