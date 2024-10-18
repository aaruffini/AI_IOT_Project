"""
This file is responsible for handling the requests to the LastFM api
"""

import requests  # Library to make HTTP Requests
# Read Key and get user agent
f = open("venv/API_KEYS")
LAST_FM_API_KEY = f.read()
USER_AGENT = 'Dataquest'
# HTTP headers
headers = {
    'user-agent': USER_AGENT
}
# HTTP payload
payload = {
    'api_key': LAST_FM_API_KEY,
    'method': 'chart.gettopartists',
    'format': 'json'
}
r = requests.get('https://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
print(r.status_code)
print("Hello LastFM")
