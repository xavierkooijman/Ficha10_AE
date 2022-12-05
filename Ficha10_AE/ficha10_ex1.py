import os

def EscreveTexto():
    '''Função que escreve num ficheiro binário o input do utilizador'''
    texto = input("Texto: ")
    f = open(ficheiro,"ab")
    f.write(bytes(texto, encoding="utf-8"))
    f.close()

def LerTexto():
    '''Função que lê o conteúdo do ficheiro binário e devolve esse conteúdo'''
    f = open(ficheiro,"rb")
    file_content = f.read()
    f.close()
    return str(file_content)

#Posionar no current working directory
path = os.getcwd()
os.chdir(path)

#Variaveis
ficheiro = "ficheiros\\dados.bin"
pasta = "ficheiros"
resp = 1

#Verificar se a pasta existe e se não criar a pasta
if not os.path.exists(pasta):
    os.mkdir(pasta)

#Ciclo while que recebe input do utilizador e corre a função adequada ao input
while(resp != 0):
    resp = int(input("MENU\n1 - Escrever\n2 - Ler\n0 - Sair\n        Opção:"))

    if(resp == 1):
        EscreveTexto()
    if(resp == 2):
        file_content = LerTexto()
        print(file_content)