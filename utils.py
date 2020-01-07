import os


def header():
    print("****************************************")
    print("*** School of Net - Caixa Eletrônico ***")
    print("****************************************")


def clear():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)
