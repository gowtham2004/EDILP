import bluetooth

def get_connected_bluetooth_device():
    """Gets the current connected Bluetooth device."""
    devices = bluetooth.discover_devices()
    for device in devices:
        if device["connected"]:
            return device
    return None

if __name__ == "__main__":
    device = get_connected_bluetooth_device()
    if device is not None:
        print(device["name"])
    else:
        print("No connected Bluetooth device")
