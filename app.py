import pandas as pd
import os
import random
import time

def definir_parametros(quantidade_parametros, lista_parametros):
    for i in range(quantidade_parametros):
        palavra_parametro = input("Insira os parâmetros a serem jogados: ")
        lista_parametros.append(palavra_parametro)
    
def mostrar_parametros(lista_parametros, letra):
    os.system('cls')
    for i in letra:
        print(f"A letra será: {i}")
    print("Os parâmetros vão ser: ")
    for i in lista_parametros:
        print(i)

def palavras_para_parametros(quantidade_parametros, dicionario, lista_parametros, letra):
    for i in range(quantidade_parametros):
        palavra_real = input(f"\nPalavra para {lista_parametros[i]}: ")
        dicionario[lista_parametros[i]] = palavra_real

def definir_letra(alfabeto):
    num = random.randrange(0,28)
    return alfabeto[num]

def bot_palavra(alfabeto):
    num = random.randrange(0, 29857)
    palavra  = alfabeto[num]
    for i in palavra:
        palavra = i
    return palavra

ent_parametros = int(input("Com quantos parâmetros vão ser jogados? "))
alfabeto = pd.read_csv("alfabeto.txt", sep = ' ').values

parametros = []
stop = {}

letra = definir_letra(alfabeto)
definir_parametros(ent_parametros, parametros)
mostrar_parametros(parametros, letra)
palavras_para_parametros(ent_parametros, stop, parametros, letra)

csv = pd.read_csv("Lista-de-Palavras.txt", sep = ' ').values


for i,j in stop.items():
    print(f"{i}: {j}")