# IN TESTING PHASE

import socket
import threading
import enigma

ip = "Your server IP"
port = 1234

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((ip, port))
socket.listen(1)
conn, addr = socket.accept()
cipher = conn.recv(1200).decode()
plain = enigma.decrypt(cipher, 20)
print(plain)
conn.close()
socket.close()