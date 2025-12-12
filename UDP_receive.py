import socketserver, json, os


# ip = "192.168.0.124"
ip = "0.0.0.0"
port = 31337

with open("hosts.json", 'r') as f:
    hosts = json.load(f)

def clear_max():
    with open("save_data.json", 'r') as save_data:
        data_table = json.load(save_data)

    for client in data_table:
        data_table[client] = 0
    with open("save_data.json", 'w') as save_data:
        json.dump(data_table, save_data)

clear_max()


class MyUDPHandler(socketserver.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        with open("save_data.json", 'r') as saved_data:
            saved_info = json.load(saved_data)

        data = self.request[0].strip()
        socket = self.request[1]
        client = hosts[self.client_address[0]]
        print(f"{hosts[self.client_address[0]]} wrote:")
        print(data)



        # saved_info["max_"+ client] = max(saved_info["max_" + client], float(str(data).split(';')[1]))
        # os.system('clear')
        # print(saved_info)
        # with open("save_data.json", 'w') as saved_data:
        #     json.dump(saved_info, saved_data)




        socket.sendto(data.upper(), self.client_address)

with socketserver.UDPServer((ip, port), MyUDPHandler) as server:
    server.serve_forever()