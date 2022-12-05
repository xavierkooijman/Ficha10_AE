import os

#Funções
def Encript(par,par2):
    '''Função que encripta o texto recebido de acordo com a chave'''
    texto = ""
    for car in par:
        val = ord(car) + par2
        texto += chr(val)

    return texto
        
def guardaFicheiro(par):
    '''Função que guarda o texto encriptado num ficheiro'''
    f = open(ficheiro,"a",encoding="utf-8")
    f.write(par)
    f.close()

def LerFicheiro():
    '''Função que lê o ficherio e devolve o seu conteúdo'''
    f = open(ficheiro,"r",encoding="utf-8")
    file_content = f.read()
    f.close()
    return file_content

def Decript(par,par2):
    '''Função que recebe o texto codificado e devolve o texto descodificado'''
    texto = ""
    for car in par:
        val = ord(car) - par2
        texto += chr(val)
    
    return texto

#Posicionar no current working directory
path = os.getcwd()
os.chdir(path)

#Variaveis
ficheiro = "ficheiros\\test.txt"
pasta = "ficheiros"
resp = 1
chave = 3

#Verificar se a pasta existe e se não criar a pasta
if not os.path.exists(pasta):
    os.mkdir(pasta)

#Ciclo while com o Menu que o utilizador interage
while(resp !=  0):
    resp = int(input("MENU\n1 - Escrever em ficheiro\n2 - Ler ficheiro\n0 - Sair\n        Opção: "))
    if(resp == 1):
        texto = input("Texto: ")
        textoCodificado = Encript(texto,chave)
        guardaFicheiro(textoCodificado)
    if(resp == 2):
        textoCodificado = LerFicheiro()
        textoDescodificado = Decript(textoCodificado,chave)
        print("Texto descodificado: ",textoDescodificado)