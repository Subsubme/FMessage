# IN TESTING PHASE

import socket
import enigma

ip = "Your server IP here"
port 1234

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = socket.connect((ip, port))

text = input("> ")
message = enigma.encrypt(text, 20)
print(f"Plain text: {text}, Ciphered text: {message}.... Sending...")
conn.send(message.encode())
conn.close()
socket.close()