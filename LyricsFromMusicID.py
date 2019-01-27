import requests

key_file = open('musixmatch-api-key', 'r')
api_key = key_file.read()
base_url = 'https://api.musixmatch.com/ws/1.1/'

track_id = raw_input('Enter the Track ID: ')

url = base_url + 'track.lyrics.get?track_id=' + track_id.strip() + '&apikey=' + api_key
response = requests.get(url)
data = response.json()
print 'Response Code:', response.status_code
print	
print data['message']['body']['lyrics']['lyrics_body']

