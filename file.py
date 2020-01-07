# from test import teste_file
# teste_file.hello_word('Leandro Tavares')

import os
from bank_account_variables import money_slips

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
