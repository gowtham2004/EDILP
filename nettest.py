import subprocess

def get_network_uid():
    """Gets the current network user ID."""
    command = ["netsh", "wlan", "show", "profile", "name=Wi-Fi", "key=ssid"]
    output = subprocess.check_output(command)
    ssid = output.decode("utf-8").strip()
    command = ["netsh", "wlan", "show", "profile", ssid, "key=uid"]
    output = subprocess.check_output(command)
    uid = output.decode("utf-8").strip()
    return uid

if __name__ == "__main__":
    uid = get_network_uid()
    print(uid)
