import socket


def get_hostname():
    hostname = socket.gethostname()
    print("host name: " + hostname)

get_hostname()