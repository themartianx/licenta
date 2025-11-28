import socket


ip = "0.0.0.0"
port = 31337
search = "True"

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((ip, port))


    while search == "True":
        data, addr = sock.recvfrom(1024)
        print("message:", data.decode('utf-8'))

        with open("switches/udpSearch.txt", "r") as f:
            search = f.read()