from fastapi import FastAPI
import requests
import json

response_API = requests.get('http://127.0.0.1:8000/')

if response_API.status_code == 200:
    data = response_API.text
    parse_json = json.loads(data)
    
    print(parse_json['data'][0]['position'])
else:
    print("Error: Could not retrieve data from API.")
