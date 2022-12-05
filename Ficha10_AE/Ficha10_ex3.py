import os
import random

def ImprimePais():

    if(count == 1):
        print("\n" + pais[0] + "-" * (comp-2))
    if(count == 2):
        print("\n" + pais[0] + pais[1] + "-" * (comp-3))
    if(count == 3):
        print("\n" + pais[0] + pais[1] + pais[2] + "-" * (comp-4))

path = os.getcwd()
os.chdir(path)

f = open("ficheiros\\paises.txt","r",encoding="utf-8")
lista = f.readlines()
f.close()
pais = str(random.choice(lista))
print(pais)
comp = len(pais)
count = 1

while(count != 4):
    ImprimePais()
    resp = input("\nQual o país: ")
    if(resp == pais):
        print("Parabens acertou!!!")
        break
    else:
        count = count + 1 