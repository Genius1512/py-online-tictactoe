# this is the client for the online tictactoe
# it handles the frontend (printing the board, asking for input) and the backend (sending the turns)

# TODO: GUI?
# TODO: Android?

from networking import Client
from functions import *
import re
from pyfiglet import figlet_format as banner
from rich import print
from socket import gethostname, gethostbyname


class App:
    def __init__(self, ip, port):
        if ip == None:
            ip = gethostbyname(gethostname())
        if port == None:
            port = 1234

        # setup
        self.client = Client()
        self.client.setup(ip, port)

        self.icon = self.client.get()
        print(f"Icon: [blue]{self.icon}[/blue]\n")
        # get board
        self.board = get_board()

        self.done = False
        while not self.done:
            # get sent data
            self.data = self.client.get()
            # your turn
            if self.data["reason"] == "your-turn":
                # output board
                self.board = self.data["board"]
                clear()
                print_board(self.board)

                print("Your turn!")
                # getting valid turn
                is_valid = False
                while not is_valid:
                    placement = input("> ").lower()
                    if (re.match("[abc][123]", placement) and self.board[list(placement)[0]][list(placement)[1]] == "-") or placement == "exit":
                        is_valid = True
                    else:
                        if placement == "exit":
                            quit()
                        else:
                            print("[red]Invalid field[/red]")

                placement = list(placement)
                self.board[placement[0]][placement[1]] = self.icon
                # send placement
                self.client.post(self.board)

                clear()
                print_board(self.board)
            # if the game ends
            elif self.data["reason"] == "end":
                state = self.data["state"]
                board = self.data["board"]
                clear()
                # print end screen
                print_board(board)
                if state == "tie":
                    print("[green]" + banner("It's a tie!") + "[/green]")
                elif state == self.icon:
                    print("[blue]" + banner("You won!") + "[/blue]")
                else:
                    print("[red]" + banner("You lost!") + "[/red]")
                quit()


if __name__ == "__main__":
    app = App(None, None)
