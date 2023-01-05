# dic = {}

# ent_parametros = int(input("Com quantos parâmetros vão ser jogados? "))

# cache = []
# parametros = []
# stop = {}

# for i in range(ent_parametros):
#     palavra_parametro = input("Insira os parâmetros a serem jogados: ")
#     parametros.append(palavra_parametro)

# for i in range(ent_parametros):
#     palavra_real = input(f"Palavra para {parametros[i]}: ")
#     dic[parametros[i]] = palavra_real

# print(dic)

# for i,j in dic.items():
#     print(i,j)

import pandas as pd
import random as rd

todas_palavras = pd.read_csv("Lista-de-Palavras.txt")

while True:
    num_aleatorio = rd.randrange(0, 29857)
    palavra = todas_palavras[num_aleatorio]