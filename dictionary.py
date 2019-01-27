import requests
import json

key_file = open('oxford-api-key', 'r')
app_id, app_key = key_file.read().split()
lang = 'en'
base_url = 'https://od-api.oxforddictionaries.com/api/v1/entries'
word = raw_input('Enter your word: ')

url = '/'.join([base_url, lang, word.lower()]) 
headers = {'app_id': app_id, 'app_key': app_key}
response = requests.get(url, headers= headers)

print("Response Code {}\n".format(response.status_code))

if response.status_code != 200:
	exit()

data = response.json()
print("Response Text \n")
for result in data['results']:
	for lexical_entry in result['lexicalEntries']:
		for entry in lexical_entry['entries']:
			for sense in entry['senses']:
				for definition in sense['definitions']:
					print(definition)