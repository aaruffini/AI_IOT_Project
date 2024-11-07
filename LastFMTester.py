"""
This file is a test to make sure the API
is working as intended.
Status code should be 200 - Ok
"""

import requests # Library to make HTTP Requests
import unittest


# Read Key and get user agent

f = open("venv/API_KEYS")
LAST_FM_API_KEY = f.readline()
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

if r.status_code == 200:
    print(r)
    print("All set!")
else:
    print(r)
    print("Check API token")








