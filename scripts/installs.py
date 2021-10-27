import os
from sys import platform


valid = False
while not valid:
    do_install = input("Do you want to install the required packages? [Y/n]").lower()
    valid = do_install in ["y", "n"]
    print("" if valid else "Invalid input")

if do_install == "n":
    quit()
else:
    os.system("pip install rich")

os.system("clear" if "win" not in platform else "cls")