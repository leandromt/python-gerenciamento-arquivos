# from test import teste_file
# teste_file.hello_word('Leandro Tavares')

import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
print(BASE_PATH)

# OPEN - funcao para abrir um arquivo existente
# 1 - passar o caminho do arquivo
# 2 - modo ( w - write, r - reader)
# file = open(BASE_PATH + '/_file_test.dat', 'w')
file = open(BASE_PATH + '/_file_test.dat', 'a')
# https://docs.python.org/3/library/functions.html?highlight=open#open
file.write('Scholl of net')
file.write('\n')
file.write('Teste 2')
file.write('\n')
file.write('teste 4')
file.writelines(('aaaaaaaaa','bbbbbbbb','cccccccc'))
file.writelines(['ddddddddd', '\n', 'eeeeeeee', '\n', 'ffffffff'])
file.close()
