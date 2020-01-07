import os

teste = os.defpath
teste2 = os.getcwd()
teste3 = os.getlogin()

# absolute path
path_absolute = os.path.abspath('.')

print(f'O caminho atual é {teste}')
print(f'O caminho atual é {teste2}')
print(f'O caminho atual é {teste3}')
print(f'O caminho absoluto é {path_absolute}')

# Exibe o caminho da pasta
print(os.path.abspath('./test/os_lib.py'))

# Exibe o caminho do diretório a partir do arquivo
file_path = os.path.abspath('./test/teste_file.py')
dir_name = os.path.dirname(file_path)
print(dir_name)

# Verifica se o caminho existe no sistema operacional
print(os.path.exists('./test'))
if os.path.exists('./test2'):
    print('A Pasta Teste Existe')
else:
    print('A Pasta Teste NAO Existe')

# Verifica se o path passado é um diretorio ou arquivo
print(os.path.isdir(dir_name))
print(os.path.isfile(dir_name))

# Exibe o nome do arquivo Corrent
print(__file__)
print(os.path.basename(__file__))

# pasta atual do arquivo
print(os.path.dirname(os.path.abspath(__file__)))