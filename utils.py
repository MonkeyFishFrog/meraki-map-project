import csv

def export_to_csv(devices, filename):
    keys = ["name", "model", "serial", "lat", "lng", "address"]
    with open(filename, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for device in devices:
            writer.writerow({k: device.get(k, "") for k in keys})
    print(f"Data exported to {filename}")