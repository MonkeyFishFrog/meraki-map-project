from meraki_api import get_devices
from map_builder import build_map
from utils import export_to_csv

devices = get_devices()
export_to_csv(devices, "data/devices.csv")
build_map(devices, "output/meraki_map.html")
