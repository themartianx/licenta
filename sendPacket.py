import socket


ip = "192.168.0.132"
port = 31337
message = "Hello world"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(message.encode(), (ip, port))