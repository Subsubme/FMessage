import socket
import enigma

ip = "Your server IP here"
port 1234

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = socket.connect((ip, port))

while True:
    message = input("> ")
    conn.send(message.encode())
    reply = conn.recv(1000).decode()
    print(reply)

conn.close()
socket.close()