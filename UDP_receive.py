import socketserver, json


ip = "192.168.0.124"
port = 31337

hosts = {}
with open("hosts.json", 'r') as f:
    hosts = json.load(f)

class MyUDPHandler(socketserver.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print(f"{hosts[self.client_address[0]]} wrote:")
        print(data)
        socket.sendto(data.upper(), self.client_address)

with socketserver.UDPServer((ip, port), MyUDPHandler) as server:
    server.serve_forever()