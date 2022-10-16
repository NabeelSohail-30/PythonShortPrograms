import uuid


def get_mac_address():
    mac = hex(uuid.getnode()).replace('0x', '').replace('L', '')
    print("mac address: " + mac)

get_mac_address()