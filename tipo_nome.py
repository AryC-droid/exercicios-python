"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

Curso: Python do Zero ao Avançado
Aula: xx - Professor Luiz Otávio Miranda

"""

nome = input('Escreva seu primeiro nome: ')

nome = int(len(nome)) #int ficou redundante / o len já retorna inteiro

if nome <= 4:
    print('Seu nome é curto')
elif nome >= 5 and nome <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande!')
