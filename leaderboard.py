from fastapi import FastAPI
import requests

response = requests.get('http://127.0.0.1:8000/')

if response.status_code == 200:
    data = response.json()
    print(type(data))
    # data.keys()
    print(data.values())
else:
    print("Error: Could not retrieve data from API.")
