from finalproject import *
from googlesheets import *
from userfunctions import *
import os


def terminal(cdict):
    """
    creates a simple terminal environment to read commands.
    params:
        cdict - a dict of commands to use, with the key as the command name and the value as the associated function
    """
    os.system('cls')
    print("Welcome to Management Software. Here are your options: \n")
    print("1. Update data")


    while True:
        instring = input("Choose an option: ")
        if instring in cdict.keys():
            cdict[instring]()
            break

cdict = {"1": update} 
terminal(cdict)
