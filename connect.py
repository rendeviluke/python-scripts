from asyncio.windows_events import ERROR_CONNECTION_ABORTED, ERROR_CONNECTION_REFUSED
import socket

ip = '127.0.0.1'
port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

message = 'Hello'

client.connect((ip, port))

client.send(message.encode())

rr = client.recv(1024)


print(rr)