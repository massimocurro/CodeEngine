import pip._vendor.requests 

def main(dict):
    response = pip._vendor.requests.get('https://function-76.1at6rgz00yjr.eu-de.codeengine.appdomain.cloud')
    return {'message': response.text}