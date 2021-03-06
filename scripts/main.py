# pyinstaller --onefile -n "Online TicTacToe" scripts/main.py
# TODO: Update exe
# TODO: Logo

from traceback import print_exc as error
import server
import client
import re
from random import randint as rint
from functions import clear, End
import ctypes


try:
    while True:
        ctypes.windll.kernel32.SetConsoleTitleW("TicTacToe")
        clear()

        is_imported = False
        while not is_imported:
            try:
                from rich import print

                is_imported = True
            except ImportError:
                print("Not all modules are installed, please install them")
                import installs
                installs.install()



        mode_is_valid = False
        while not mode_is_valid:
            mode = input("Enter mode: ")
            mode_is_valid = mode in ["client", "server", "exit"]
            print("[red]Invalid" if not mode_is_valid else "")

        if mode == "client":
            ctypes.windll.kernel32.SetConsoleTitleW("TicTacToe - Client")
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
            
            clear()
            app = client.App(ip, port)

        elif mode == "server":
            ctypes.windll.kernel32.SetConsoleTitleW("TicTacToe - Server")
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

            clear()
            app = server.App(port)
        
        elif mode == "exit":
            raise End()

        else:
            raise Exception("Fuck")
        
        input("Enter to restart\n")


except End:
    print("\nEnter to quit")
    input("")

except Exception as e:
    error()
    print("\n\n[red]An error occured. Please report this to Silvan Schmidt")
    input("Enter to quit")
