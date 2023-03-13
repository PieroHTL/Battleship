import socket, threading

class MyServer:
    def __init__(self, host, port):
        #Initialize the server object with a hostname and port number
        self.host =host
        self.port =port
        self.socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen()

        print(f"Server started on {self.host}:{self.port}")

    def run(self):
        while(True):
            #Waiting for a client to connect and get the client socket and address names 
            client_socket, client_address = self.socket.accept() #Name should be added from login page in the future
            print(f"New client connected: {client_address[0]}:{client_address[1]}") #Maybe name at [2]?
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        while(True):
            data =client_socket.recv(1024)
            if(not data):
                break

            x, y =map(int, data.decode().split(',')) #Parses the received data as x and y coordinates
            print(f"Received shot from client {client_socket.getpeername()[0]}: {x}, {y}")

            response ="OK"
            client_socket.send(response.encode())

        print(f"Client {client_socket.getpeername()[0]} disconnected")
        client_socket.close()

if __name__ == '__main__':
    server =MyServer('localhost', 6002)
    server.run()