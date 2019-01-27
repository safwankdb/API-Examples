import requests
import html2text

h = html2text.HTML2Text()
key = open('google-api-key', 'r')
apiKey = key.read()

origin = raw_input('Origin: ')
destination = raw_input('Destination: ')

url = 'https://maps.googleapis.com/maps/api/directions/json?origin='+origin+'&destination='+destination+'&key='+apiKey

r = requests.get(url)
data = r.json()['routes'][0]
print('\n' + data['summary'])
for legs in data['legs']:
	for steps in legs['steps']:
		print(h.handle(steps['html_instructions']))
