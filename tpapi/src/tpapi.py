import requests
import base64
import time
from enum import Enum

class Environment(Enum):
    DEV = ""
    LAB = ""
    PRODUCTION = "https://api.tierpoint.com/api/v1/"

class TPAPI():
    def __init__(self, env):
        self.environment = env
        self.auth = {}
        self.endpoints = {
            "oauth": {
                "token": "oauth/token/"
            }
        }

        self.oauth = OAuth(self)

    def isTokenExpired():
        return(int(time.time()) > self.auth["expiresAt"])

class OAuth:
    def __init__(self, obj):
        self.tpapi_obj = obj

    def getToken(self, username, password, encode_password):
        if encode_password: password = base64.b64encode(bytes(password, 'utf-8'))
        response = requests.post(self.tpapi_obj.environment.value + self.tpapi_obj.endpoints["oauth"]["token"], json={"userName": username, "password": password})

        if response.status_code == requests.codes.ok:
            self.tpapi_obj.auth["token"] = "Bearer: " + response.json()["token"]
            self.tpapi_obj.auth["expiresIn"] = response.json()["expiresIn"]
            self.tpapi_obj.auth["expiresAt"] = response.json()["expiresAt"]
            return(self.tpapi_obj.auth["token"])

        return response.text