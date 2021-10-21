from socket import *
from random import randint as rint


class CustomError(Exception):
    pass


class Server:
    def __init__(self):
        self.ip, self.port = None, None
        self.connections = {}

        self.setup()

    def setup(self):
        self.ip, self.port = self.get_inf(1512)

        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(2)
        print("Server open\n")

    def get_inf(self, port="random"):
        if port == "random":
            port = rint(1000, 5000)
        ip = gethostbyname(gethostname())
        print(f"IP: {ip}; Port: {port}")

        return ip, port

    def new_connection(self, id: str):
        if id in self.connections:
            raise CustomError("Id already used")
        else:
            self.connections[id], (remotehost, remoteport) = self.server.accept()

            print(f"{self.connections[id].recv(1024).decode()} connected with id '{id}'")

    def get(self, id: str):
        return self.connections[id].recv(1024).decode()

    def post(self, ids: list, content: str):
        for id in ids:
            if id in self.connections:
                self.connections[id].send(content.encode())


class Client:
    def __init__(self):
        self.ip, self.port = self.get_inf("dbug")

        self.client = socket(AF_INET, SOCK_STREAM)
        self.connect()

    def get_inf(self, mode="custom"):
        if mode == "custom":
            ip = input("Enter ip: ")
            port = int(input("Port: "))
        elif mode == "dbug":
            ip = gethostbyname(gethostname())
            port = 1512
        return ip, port

    def connect(self):
        self.client.connect((self.ip, self.port))
        self.client.send(gethostbyname(gethostname()).encode())
        print(f"Connected to {self.ip}\n")

    def get(self):
        msg = self.client.recv(1024).decode()
        return msg

    def post(self, content: str):
        self.client.send(content.encode())


if __name__ == "__main__":
    server = Server()
