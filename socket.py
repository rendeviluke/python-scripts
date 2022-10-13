import socket

ip = '127.0.0.1'
port = 999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print("Connecting...")
s.connect((ip, port))