from file import open_file_bank, write_money_slips
from utils import header


def main():
    header()
    make_money_slips()


def make_money_slips():
    file = open_file_bank('w')
    write_money_slips(file)
    print('Cédulas gravas com sucesso!')

main()
