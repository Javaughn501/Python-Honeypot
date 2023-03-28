import socket
import threading
import logging

logging.basicConfig(filename='honeypot.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

ports = [22,80,443,8080]
sockets = []

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", port))
    s.listen()
    sockets.append(s)
    print("Listening on port %s" % port)

    
def runSocket(socket):
    while True:
        conn, addr = socket.accept()
        logging.info('Connection from %s' % addr[0])
        print(conn)
        # print ("Connection from %s" % addr[0])
        data = conn.recv(1024)
        logging.info('Data: %s' % data.decode())
        # print("Received data: %s" % data.decode())
        conn.close()

for s in sockets:
    t = threading.Thread(target=runSocket, args=(s,))
    t.start()