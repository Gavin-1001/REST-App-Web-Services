import socket

def hpping():
    ip = socket.gethostbyname(socket.gethostname())
    return ip
