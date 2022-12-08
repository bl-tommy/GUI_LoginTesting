import socket
import main

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 25545))

message = client.recv(1024).decode()
client.send(input(message).encode())
message = client.recv(1024).decode()
client.send(input(message).encode())
print("client.recv(1024)".decode())
