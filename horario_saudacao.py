"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

Curso: Python do Zero ao Avançado
Aula: 32 - Professor Luiz Otávio Miranda
"""

horario_atual = input('Informe a hora cheia ')

try:
    horario_atual = int(horario_atual)
    bom_dia = (horario_atual >= 0) and (horario_atual <= 11)
    boa_tarde = (horario_atual >= 12) and (horario_atual <= 17)
    boa_noite = (horario_atual >= 18) and (horario_atual <=23)

    if bom_dia:
        print('Bom dia!')
    elif boa_tarde:
        print('Boa tarde!')
    elif boa_noite:
        print('Boa noite!')
    else:
        print('Horário não existe!')

except:
    print('Formato inválido / não solicitado')
