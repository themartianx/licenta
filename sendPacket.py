import socket, time
import getInfo

ip = "192.168.0.124"
port = 31337
message = getInfo.systemInfo()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(message.encode(), (ip, port))

while True:
    message = getInfo.upadteInfo()
    time.sleep(2)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (ip, port))