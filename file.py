# from test import teste_file
# teste_file.hello_word('Leandro Tavares')

import os
from bank_account_variables import money_slips, accounts_list

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
print(BASE_PATH)

# OPEN - funcao para abrir um arquivo existente
# 1 - passar o caminho do arquivo
# 2 - modo ( w - write, r - reader)
# file = open(BASE_PATH + '/_file_test.dat', 'w')
# file = open(BASE_PATH + '/_file_test.dat', 'a')
# https://docs.python.org/3/library/functions.html?highlight=open#open
# file.write('Scholl of net')
# file.write('\n')
# file.write('Teste 2')
# file.write('\n')
# file.write('teste 4')
# file.writelines(('aaaaaaaaa','bbbbbbbb','cccccccc'))
# file.writelines(['ddddddddd', '\n', 'eeeeeeee', '\n', 'ffffffff'])
# file.close()

# file = open(BASE_PATH + '/_file_test.dat', 'r')  # read
# print(file.read())  # read all file

# print(file.read(50)) # read some caracters
# print(file.read(50)) # read some caracters continues

# print(file.readline()) # read one line
# print(file.readline()) # read next line

# print(file.readline(7))
# print(file.readline(2))
# print(file.readline(15))

# print(file.readlines())  # texto to list
# linhas = file.readlines()

# file.close()

# print(linhas[2])
# for l in linhas:
    # print(l)


def open_file_bank(mode):
    return open(BASE_PATH + '/_bank_file.dat', mode)


#20=5;50=5;100=5
def write_money_slips(file):
    for money_bill, value in money_slips.items():
        file.write(money_bill+'='+str(value)+';')


def write_bank_accounts(file):
    for account, account_data in accounts_list.items():
        file.writelines((
            account, ';',
            account_data['name'], ';',
            account_data['password'], ';',
            str(account_data['value']), ';',
            str(account_data['admin']), ';'
            '\n'
        ))


def read_money_slips(file):
    line = file.readline()
    while line.find(';') != -1:
        semicolon_pos = line.find(';')
        money_bill_value = line[0:semicolon_pos]
        set_money_bill_value(money_bill_value)
        # 20=5000;50=5000
        if semicolon_pos + 1 == len(line):
            break
        else:
            line = line[semicolon_pos + 1:len(line)]


def set_money_bill_value(money_bill_value):
    equals_pos = money_bill_value.find('=')  # 20=5000
    money_bill = money_bill_value[0:equals_pos]
    count_money_bill_value = len(money_bill_value)
    value = money_bill_value[equals_pos + 1:count_money_bill_value]
    print(money_bill, value)
    money_slips[money_bill] = int(value)


def read_bank_accounts(file):
    lines = file.readlines()
    lines = lines[1:len(lines)]
    for account_line in lines:
        extract_bank_account(account_line)


def extract_bank_account(account_line):
    account_data = []
    while account_line.find(';') != -1:
        semicolon_pos = account_line.find(';')
        data = account_line[0:semicolon_pos]
        account_data.append(data)
        if semicolon_pos + 1 == len(account_line):
            break
        else:
            account_line = account_line[semicolon_pos + 1:len(account_line)]
    add_bank_account(account_data)


def add_bank_account(account_data):
    accounts_list[account_data[0]] = {
        'name': account_data[1],
        'password': account_data[2],
        'value': float(account_data[3]),
        'admin': bool(account_data[4])
    }


def load_bank_data():
    file = open_file_bank('r')
    read_money_slips(file)
    file.close()

    file = open_file_bank('r')
    read_bank_accounts(file)
    file.close()
