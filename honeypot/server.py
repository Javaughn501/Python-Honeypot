import socket
import logging
from threading import Thread

from pydivert import WinDivert  # type: ignore

from constants import PORTS


def capture_packets():
    win_divert_filter = (
        "(tcp.DstPort == 22 or "
        "tcp.DstPort == 80 or "
        "tcp.DstPort == 443 or "
        "tcp.DstPort == 8080) and "
        "tcp.PayloadLength > 0"
    )

    win_divert = WinDivert(win_divert_filter)
    win_divert.open()

    for _ in range(10):
        packet = win_divert.recv()
        print(packet)

    win_divert.close()


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

    capture_packets()
