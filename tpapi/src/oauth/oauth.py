import config
import requests

def getToken(username, password, encode_password):
    if encode_password: password = base64.b64encode(bytes(password, 'utf-8'))