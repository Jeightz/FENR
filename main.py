from model import models  
import requests
import json
from flask import Flask
import os 
from fetch import fetch

fetchapi = fetch()
app = Flask(__name__)
@app.route("/fetch/<path:key>")

def fetch_key(key):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, "api.json")
    with open(json_path, "r") as file:
        data = json.load(file)    
    for keys in data:
        if keys == key:
            return fetchapi.fetch_api_data(key)
    
    


if __name__ == "__main__":


    app.run(debug=True)
   
    