import os

path = os.getcwd()
os.chdir(path)

resp = 1

while(resp != 0):
    resp = int(input("1 - Inserir país\n0 - Sair\n        Opção: "))
    if(resp == 1):
        pais = input("Insira um país: ")
        f = open("ficheiros\\paises.txt", "a", encoding="utf-8")
        f.write(pais + "\n")
        f.close()