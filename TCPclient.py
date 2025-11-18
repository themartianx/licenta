import socket

ip = '127.0.0.1'
port = 65432
message = "hello world"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((ip, port))
    sock.sendall(message.encode())
    data = sock.recv(1024)

print(f"received {data!r}")