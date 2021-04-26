import requests
import json

server = "http://localhost:8000/"

machineID = json.loads(requests.get(server + "getid").content)['id']

data = str(machineID) + "\ntrains,2\ntemperature,20\ndicks,2"

requests.post(server + "receive_data", data=data)

