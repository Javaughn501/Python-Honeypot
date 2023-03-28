import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 22))
s.sendall(b'Sending message to port 22')
s.close()
