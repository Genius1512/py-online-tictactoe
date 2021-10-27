# a script for simpliefiying the communication between the server and the client
# server:
#   setup() -> inits the server
#   new_connection() -> adds a new connection to the server with the given id
#   get() -> tries to get the a message from the client with the specified id
#   post() -> sends a message to the clients with the given id(s)
#
# client:
#    setup() -> inits the client
#    connect() -> conntects to the server with the specified ip and port
#    get() -> tries to get a message from the server
#    post() -> sends a message to the server

from socket import *
from pickle import loads, dumps
from rich import print


class Server:
    def __init__(self):
        self.ip, self.port = None, None
        self.connections = {}

    def setup(self, ip=gethostbyname(gethostname()), port=1234, listen_to=5):
        self.ip, self.port = ip, port
        # create server
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(listen_to)
        print(f"[white]Server open with IP [blue]{self.ip}[/blue] on Port [blue]'{self.port}'[/blue]\n")

    def new_connection(self, id: str):
        # validate id
        if id in self.connections:
            print("[red]Id already used")
            exit()
        else:
            print(f"[white]Waiting for new connection with id [blue]{id}[/blue]")
            self.connections[id], (remotehost, remoteport) = self.server.accept() # accepting the next connection
            print(f"[white][blue]{remotehost}[/blue] connected with id [blue]'{id}'[/blue]\n")

    def get(self, id: str): # get a message
        return loads(self.connections[id].recv(1024))

    def post(self, ids: list, content: str): # post a message to the specified clients
        for id in ids:
            if id in self.connections:
                self.connections[id].send(dumps(content))


class Client:
    def __init__(self):
        self.ip, self.port = None, None

    def setup(self, ip=gethostbyname(gethostname()), port=1234):
        self.ip, self.port = ip, port
        # create client and connect to server
        self.client = socket(AF_INET, SOCK_STREAM)
        self.connect()

    def connect(self):
        self.client.connect((self.ip, self.port))
        print(f"[white]Connected to [blue]{self.ip}[/blue] on port [blue]{self.port}[/blue]\n")

    def get(self):
        return loads(self.client.recv(1024)) # get a message from the server

    def post(self, content: str):
        self.client.send(dumps(content)) # send a message to the server
