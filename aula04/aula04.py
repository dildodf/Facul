'''
Elabore um programa que receba a idade de u cidadão e verifique de acordo com as situações abaixo:
Menor que 16 anos  apresenta somente 'não vota'
maior que 18 apresenta 'voto obrigatório'
'''
'''
idade = int(input('Informe a idade: '))

if idade < 16:
    print('nao vota.')
if idade > 18:
    print('voto obrigatorio.')
'''
#-----------------------------------------------------------------------
'''
Elabore um programa que receba a idade de u cidadão e verifique de acordo com as situações abaixo:
Menor que 16 anos  apresenta somente 'não vota'
maior que 17 apresenta 'voto obrigatório'
16 ou 17 opcional
'''
#Forma 1
'''
idade = int(input('Informe a idade:'))

if idade < 16:
    print('Não vota.')
if idade > 17:
    print('Voto obrigatório.')
if idade == 16:
    print('Opcional.')
if idade == 17:
    print('Opcional.')
'''
#Forma 2 usando o else
'''
idade = int(input('Informe a idade:'))

if idade < 16:
    print('Não vota.')
else:
    if idade > 17:
        print('Obrigatório.')
    else:
        print('Opcional')
'''
#-----------------------------------------------------------------------
'''
Elabore um programa que receba a idade de u cidadão e verifique de acordo com as situações abaixo:
1- idade negativa 'não nasceu'
2- Menor que 16 anos  apresenta somente 'não vota'
3- maior que 17 apresenta 'voto obrigatório'
4- 16 ou 17 opcional
5- Maior que 60 somente 'opcional'
6- caso tenha 37 somente 'ganha ganha premio e não vota'
7- 74 voto obrigatório, no entanto 'recebe premio'.
'''
#Forma 1
idade = int(input('Informe a idade:'))

if idade < 0:
    print('Não nasce.')
else:
    if idade < 16:
        print('Não vota.')
    else:
        if idade < 18:
            print('Opcional.')
        else:
            if idade < 61:
                if idade == 37:
                    print('prêmio e não vota')
                else:
                    print('obrigatório')
            else:
                if idade == 74:
                    print('prêmio, voto é obrigatório')
                else:
                    print('opcional')
                    
            






















#Forma 2
'''
idade = int(input('Informe a idade:'))

if idade < 16:
    print('Não vota.')
else:
    if idade > 17:
        print('Obrigatório.')
    else:
        print('Opcional')
'''
