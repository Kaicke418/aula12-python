import os
import shutil
# **Exercício 1: Criar e ler um Arquivo**

# with open('novo.txt', 'w') as arq:
#     m = arq.read()
#     print(m)


# with open('novo.txt', 'r') as arq:
#     m = arq.read()
#     print(m)    

# **Exemplo 2: Cria um Diretório**

# os.mkdir('diretorio')

# **Exercício 3: Renomear um Diretório**

# os.rename('diretorio', 'teste')

# **Exercício 4:   Listar Arquivos em um Diretório** 
# with os.scandir('teste') as diretorio:
#     for arquivo in diretorio:
#         if arquivo.is_file():
#             print(arquivo)

# **Exercício 5: copiar Arquivos em um Diretório** 

# shutil.copytree('teste', 'diretorio')

# **Exercício 6: remover**

shutil.rmtree('teste')