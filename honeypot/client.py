import socket

from constants import PORTS


def start():
    for port in PORTS:
        client_socket = socket.socket()
        client_socket.connect(("localhost", port))
        client_socket.sendall(b"I am a client connected to port %d" % port)
        client_socket.close()
