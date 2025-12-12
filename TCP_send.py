import socket, sys

ip = "192.168.0.171"
port = 65432
message = "requestSystemInfo"

data = " ".join(sys.argv[1:])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((ip, port))
    sock.sendall(bytes(data, "utf-8"))
    sock.sendall(b"\n")


    received = str(sock.recv(1024), "utf-8")

print("Sent:    ", data)
print("Received:", received)