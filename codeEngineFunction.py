import sys
import requests
import json
from cryptography.fernet import Fernet

def main(dict):
    headers = {"Content-Type": "application/json"}
    response = requests.post("https://isp-dev01.op.ibmcloud.com/grc/ext/LDCImport/data", headers=headers, auth=("U0L9010", "Intesa2022!"), data=json.dumps([{'fileName': "Pandora_DL_OP_20231103170757.csv", 'group':"Default"}]))
    return {'message': response.text}
