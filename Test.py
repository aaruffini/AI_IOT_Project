import requests
from io import BytesIO

# Fetch the currently playing track from Last.fm
f = open("API_KEYS")
API_KEY = f.readline()
USERNAME = f.readline()
url = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={USERNAME}&api_key={API_KEY}&format=json'

response = requests.get(url)
data = response.json()

# Get the album cover URL of the current song
album_cover_url = data['recenttracks']['track'][0]['image'][-1]['#text']
print(album_cover_url)




