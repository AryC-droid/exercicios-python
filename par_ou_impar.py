"""
Exercício
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.


Curso: Python do Zero ao Avançado
Aula: 32 - Professor Luiz Otávio Miranda
"""

numero = input('Digite um número inteiro: ')

try:
    numero = int(numero)
    resultado = numero % 2 == 0

    if resultado == True: # ficou redundante
        print('Esse número é par')
    else:
        print('Esse número é impar')

except:
    print('Não é um numero inteiro')
