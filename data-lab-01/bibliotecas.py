import numpy as np
from math import *
from random import choice, randrange

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

escolha = choice(lista)
print(escolha)

escolha2 = randrange(100)
print(escolha2)

print("Digite um número: ")
numero1 = int(input())
print("Digite outro número: ")
numero2 = int(input())
resultadoPotencia = pow(numero1, numero2)
print(f"O número {numero1} elevado a {numero2} tem como resultado: {resultadoPotencia}!")

print("Qual é o número de pessoas sorteadas? ")
sorteados = int(input())
escolhaSorteio = randrange(sorteados)
print(f"O número sorteado foi: {escolhaSorteio}!")

token = randrange(1000, 10000, 2)
print("Digite o seu nome: ")
nome = input()
print(f"Olá, {nome}, o seu token de acesso é {token}! Seja bem-vindo(a)!")