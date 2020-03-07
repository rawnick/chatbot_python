import json, requests

url = 'http://ipinfo.io/json'
response = requests.get(url)
data = response.json()

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']

def getCityFromIP():
    return city

def getIP():
    return IP