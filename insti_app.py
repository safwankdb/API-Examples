import requests
from tabulate import tabulate

URL = 'https://api.insti.app/api/events'

response = requests.get(URL)
data = response.json()
print 'Response Code:', response.status_code, '\n'

for event in data['data']:
	print('%s %1i' % (event['name'], event['going_count']))