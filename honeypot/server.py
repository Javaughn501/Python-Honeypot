import socket
import logging
from threading import Thread

from constants import PORTS


def handle_request(server_socket: socket.socket):
    connection, address = server_socket.accept()

    logging.info(f"Connection from {address[0]} remote port {address[1]}")
    print(f"Connection from {address[0]} remote port {address[1]}")

    data = connection.recv(1024).decode()

    logging.info(f"Data: {data}")
    print(f"Data: {data}")

    connection.close()


def start():
    logging.basicConfig(
        filename="honeypot.log",
        filemode="w",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )

    for port in PORTS:
        server_socket = socket.socket()
        server_socket.bind(("", port))
        server_socket.listen()

        print(f"Listening on port {port}")

        Thread(target=handle_request, args=(server_socket,)).start()
