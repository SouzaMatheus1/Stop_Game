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
    print(f"A letra será: {letra}")
    print("Os parâmetros vão ser: ")
    for i in lista_parametros:
        print(i)

def palavras_para_parametros(quantidade_parametros, dicionario, lista_parametros, letra):
    for i in range(quantidade_parametros):
        palavra_real = input(f"\nPalavra para {lista_parametros[i]}: ")
        dicionario[lista_parametros[i]] = palavra_real

def definir_letra(alfabeto):
    num = random.randrange(0,28)
    letra = alfabeto[num]
    for i in letra:
        letra = i
    return letra

def bot_palavra(todas_palavras, letra):
    on = True
    while on:
        num = random.randrange(0, 29857)
        palavra  = todas_palavras[num]
        for i in palavra:
            palavra = i
        if palavra[0] == letra.upper():
            return palavra
        else:
            continue

def jogada_pc():
    pass

ent_parametros = int(input("Com quantos parâmetros vão ser jogados? "))
alfabeto = pd.read_csv("alfabeto.txt", sep = ' ').values

parametros = []
stop_p1 = {}
stop_pc = {}

letra = definir_letra(alfabeto)
definir_parametros(ent_parametros, parametros)
mostrar_parametros(parametros, letra)
palavras_para_parametros(ent_parametros, stop_p1, parametros, letra)

csv = pd.read_csv("Lista-de-Palavras.txt", sep = ' ').values

for i,j in stop_p1.items():
    print(f"Jogador: {i} = {j}")
    
for i,j in stop_pc.items():
    print(f"PC: {i} = {j}")    