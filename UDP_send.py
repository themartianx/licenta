import socket, sys, getInfo

ip = "192.168.0.124"
port = 31337
data = " ".join(sys.argv[1:])

# SOCK_DGRAM is the socket type to use for UDP sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# As you can see, there is no connect() call; UDP has no connections.
# Instead, data is directly sent to the recipient via sendto().

while True:
    data = getInfo.updateInfo()
    sock.sendto(bytes(data + "\n", "utf-8"), (ip, port))
    received = str(sock.recv(1024), "utf-8")

    print("Sent:    ", data)
    print("Received:", received)