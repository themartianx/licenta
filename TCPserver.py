import socket

ip = "127.0.0.1"
port = 65432
search = True
while search == "True":
    print("connecting...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((ip, port))
        sock.listen()
        conn, addr = sock.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                print("Received: " + str(data))
                if not data:
                    break
                conn.sendall(data)

        with open("tcpSearch.txt", "r") as f:
            search = f.read()
            print("search: " + search)

