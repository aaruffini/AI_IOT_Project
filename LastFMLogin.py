import requests
import webbrowser

def get_token(API_KEY, API_SECRET, SCROBURL):
    params = {
        'method': 'auth.getToken',
        'api_key': API_KEY,
        'format': 'json'
    }
    response = requests.get(SCROBURL, params=params)
    data = response.json()
    return data['token']

def user_authentication(token, API_KEY):
    auth_url = f"https://www.last.fm/api/auth/?api_key={API_KEY}&token={token}"

def login():
    f = open("venv/API_KEYS")
    API_KEY = f.readline()
    API_SECRET = f.readline()
    SCROBURL = 'http://ws.audioscrobbler.com/2.0/'

    token = get_token(API_KEY, API_SECRET, SCROBURL)
    user_authentication(token, API_KEY)
