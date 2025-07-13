import requests
from config import API_KEY, HEADERS, NETWORK_ID

def get_devices():
    url = f"https://api.meraki.com/api/v1/networks/{NETWORK_ID}/devices"
    response = requests.get(url, headers=HEADERS)
    return response.json()
