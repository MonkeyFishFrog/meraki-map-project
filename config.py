from dotenv import load_dotenv
import os

load_dotenv()  # load variables from .env

API_KEY = os.getenv("MERAKI_API_KEY")
NETWORK_ID = os.getenv("MERAKI_NETWORK_ID")
HEADERS = {
    "X-Cisco-Meraki-API-Key": API_KEY,
    "Content-Type": "application/json"
}
