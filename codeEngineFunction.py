import sys
import json
import pip._vendor.requests

app = Flask(__name__)

@app.route("/")
def callFunction(dict):
    headers = {"Content-Type": "application/json"}
    response = pip._vendor.requests.get("https://function-76.1at6rgz00yjr.eu-de.codeengine.appdomain.cloud")
    return {'message': response.text}
