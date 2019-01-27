import requests
from pprint import pprint

key_file = open('openweather-api-key', 'r')
api_key = key_file.read().strip()
print(api_key)
base_url = 'http://api.openweathermap.org/data/2.5/weather?q='
city = raw_input('Enter City: ')
url = base_url+city+'&APPID='+api_key
response = requests.get(url)
data = response.json()
pprint(data)
