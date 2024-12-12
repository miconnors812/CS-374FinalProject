def testprint():
    print("Test")

def terminal(cdict):
    """
    creates a simple terminal environment to read commands.
    params:
        cdict - a dict of commands to use, with the key as the command name and the value as the associated function
    """
    while True:
        instring = input()
        if instring in cdict.keys():
            cdict[instring]()
            break

cdict = {"test": testprint} ##TODO: fill in
terminal(cdict)
