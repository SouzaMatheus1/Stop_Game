import pandas as pd
import random as rd

csv = pd.read_csv("Lista-de-Palavras.txt", sep = ' ').values

dic = {}

ent_parametros = int(input("Com quantos parâmetros vão ser jogados? "))

cache = []
parametros = []
stop = {}

alfabeto = pd.read_csv("alfabeto.txt", sep = ' ').values
num = rd.randrange(0,25)
letra = alfabeto[num]

for i in letra:
    letra = i

print(letra)

# for i in range(ent_parametros):
#     palavra_parametro = input("Insira os parâmetros a serem jogados: ")
#     parametros.append(palavra_parametro)

# for i in range(ent_parametros):
#     palavra_real = input(f"Palavra para {parametros[i]}: ")
#     if palavra_real[0].upper() == letra:
#         print('cu')
#     else:
#         print('cuzin')
#     dic[parametros[i]] = palavra_real

# for i,j in dic.items():
#     print(i,j)
    
on = True
while on:
    num = rd.randrange(0, 29857)
    palavra  = csv[num]
    for i in palavra:
        palavra = i
    if palavra[0] == letra:
        on = False

print(palavra)
