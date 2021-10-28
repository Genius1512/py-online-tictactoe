import os
from sys import platform
import pip


def install():
    valid = False
    while not valid:
        do_install = input("Do you want to install the required packages? [Y/n]").lower()
        valid = do_install in ["y", "n"]
        print("" if valid else "Invalid input")

    if do_install == "n":
        quit()
    else:
        for package in ["rich"]:
            pip.main(["install", package])

    os.system("clear" if "win" not in platform else "cls")