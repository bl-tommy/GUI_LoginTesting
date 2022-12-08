import socket
import main

client = socket.socket(socket.AF_INET, socket.SOCKL_STREAM)
client.connect(("localhost", 9999))

message = client.recv(1024).decode()
client.send(input(message).encode())
message = client.recv(1024).decode()
client.send(input(message).encode())
print("client.recv(1024)".decode())
