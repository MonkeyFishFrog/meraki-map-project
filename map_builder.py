import folium

def build_map(devices, output_file):
    m = folium.Map(location=[37.77, -122.41], zoom_start=4)
    for device in devices:
        if "lat" in device and "lng" in device:
            folium.Marker(
                [device["lat"], device["lng"]],
                popup=f"{device['name']} ({device['model']})",
                tooltip=device['serial']
            ).add_to(m)
    m.save(output_file)
