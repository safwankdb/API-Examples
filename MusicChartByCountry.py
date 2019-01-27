import requests
from pprint import pprint

key_file = open('musixmatch-api-key', 'r')
api_key = key_file.read()
base_url = 'https://api.musixmatch.com/ws/1.1/'

country = 'ww'
'''
in - India
us - USA
uk - UK
it - Italy
ww - Worldwide
'''
n_songs = raw_input('Enter number of top tracks: ')

headers = {'apikey': api_key, 'country': 'in'}

url = base_url + 'chart.tracks.get?chart_name=top&page=1&page_size='+n_songs+'&country='+country+'&f_has_lyrics=1' + '&apikey=' + api_key
response = requests.get(url)
data = response.json()
print 'Response Code:', response.status_code
for track in data['message']['body']['track_list']:
	track_data = track['track']
	print 
	print 'Track Name :', track_data['track_name']
	print 'Track ID :', track_data['track_id']
	print 'Album Name :', track_data['album_name']
	print 'Artist Name :', track_data['artist_name']

