# this is the client for the online tictactoe
# it handles the frontend (printing the board, asking for input) and the backend (sending the turns)

from high_lvl_networking import Client
from functions import *
import re
from socket import gethostname, gethostbyname
from rich import print


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
        print(f"[white]Icon: [blue]{self.icon}[/blue]\n")
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

                print("[white]Your turn!")
                placement = self.get_turn()

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
                    print("" + "It's a tie!" + "")
                elif state == self.icon:
                    print("" + "You won!" + "")
                else:
                    print("" + "You lost!" + "")
                self.done = True

    def get_turn(self, mode="text"):
        # getting valid turn
        if mode == "text":
            is_valid = False
            while not is_valid:
                placement = input("> ").lower()
                is_valid = (re.match("[abc][123]", placement) and self.board[list(placement)[0]][list(placement)[1]] == "-") or placement == "exit"
                print("[red]Invalid field" if not is_valid else "")
                    
            if placement == "exit":
                raise End()

            placement = list(placement)

        elif mode == "gui":
            placement = ["a", "1"]

        return placement


if __name__ == "__main__":
    app = App(None, None)
