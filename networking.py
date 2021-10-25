from socket import *
from random import randint as rint
from rich import print


class CustomError(Exception):
    pass


class Server:
    def __init__(self):
        self.ip, self.port = None, None
        self.connections = {}

    def setup(self, ip=gethostbyname(gethostname()), port=1234):
        self.ip, self.port = ip, port

        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(2)
        print(f"Server open with IP [blue]{self.ip}[/blue] on Port '[blue]{self.port}[/blue]'\n")

    def new_connection(self, id: str):
        if id in self.connections:
            print("[red]Id already used[/red]")
            exit()
        else:
            print(f"Waiting for new connection with id [blue]{id}[/blue]")
            self.connections[id], (remotehost, remoteport) = self.server.accept()

            print(f"[blue]{self.connections[id].recv(1024).decode()}[/blue] connected with id '[blue]{id}[/blue]'\n")

    def get(self, id: str):
        return self.connections[id].recv(1024).decode()

    def post(self, ids: list, content: str):
        for id in ids:
            if id in self.connections:
                self.connections[id].send(content.encode())


class Client:
    def __init__(self):
        self.ip, self.port = None, None

    def setup(self, ip=gethostbyname(gethostname()), port=1234):
        self.ip, self.port = ip, port

        self.client = socket(AF_INET, SOCK_STREAM)
        self.connect()

    def connect(self):
        self.client.connect((self.ip, self.port))
        self.client.send(gethostbyname(gethostname()).encode())
        print(f"Connected to [blue]{self.ip}[/blue]\n")

    def get(self):
        msg = self.client.recv(1024).decode()
        return msg

    def post(self, content: str):
        self.client.send(content.encode())


if __name__ == "__main__":
    server = Server()
