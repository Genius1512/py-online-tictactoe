from traceback import print_exc as error
import server
import client
import re
from sys import platform
from random import randint as rint
from os import system


try:
    def cls():
        system("clear" if "win" not in platform else "cls")
    cls()

    is_imported = False
    while not is_imported:
        try:
            from rich import print

            is_imported = True
        except ImportError:
            print("Not all modules are installed, please install")
            import installs
            installs.install()



    mode_is_valid = False
    while not mode_is_valid:
        mode = input("Enter mode: ")
        mode_is_valid = mode in ["client", "server"]
        print("[red]Invalid" if not mode_is_valid else "")

    if mode == "client":
        ip_is_valid = False
        while not ip_is_valid:
            ip = input("Ip: ")
            ip_is_valid = re.match("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip) or ip == "self"
            if ip == "self":
                from socket import gethostbyname, gethostname
                ip = gethostbyname(gethostname())
            print("[red]Invalid" if not ip_is_valid else "")

        port_is_valid = False
        while not port_is_valid:
            try:
                port = int(input("Port: "))
                port_is_valid = 1000 <= port <= 5000
                print("[red]Invalid" if not port_is_valid else "")
            except TypeError:
                print("[red]Invalid")
        
        cls()
        app = client.App(ip, port)

    elif mode == "server":
        port_is_valid = False
        while not port_is_valid:
            port = input("Port: ")
            try:
                port_is_valid = 1000 <= int(port) <= 5000 or port == "random"
            except ValueError:
                port_is_valid = port == "random"
            print("[red]Invalid" if not port_is_valid else "")
        if port == "random":
            port = rint(1000, 5000)
        else:
            port = int(port)

        cls()
        app = server.App(port)

    else:
        raise Exception("Fuck")
except Exception as e:
    error()
    print("\n\n[red]An error occured. Please report this to Silvan Schmidt")
    input("Enter to quit")