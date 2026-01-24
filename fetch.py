import json
import requests
import os
from model import models

class fetch():
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(current_dir, "api.json")
        with open(json_path,"r") as file:
            self.data =json.load(file)
        self.model = models()
        
    def fetch_api_data(self,key):
        checkkey =self.model.findkey(key)
        if checkkey:
            return checkkey
        
        api = self.data[key]
        if not api:
            return {"Error Api": "API not found"}
        fetchs = requests.get(api)
        data =fetchs.json()
        
        self.model.addkeyvalue(key,json.dumps(data))
        return data
     