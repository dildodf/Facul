#uso de números quebrados
# v1 = float(input('Informe o primeiro valor:' ))
#v2 = float(input('Informe o primeiro valor:' ))
#uso de números inteiros
print('---------------------------------')
print('MASTER CALC 2024 - TURBO EDITION')
print('---------------------------------')
v1 = int(input('Informe o primeiro valor:' ))
v2 = int(input('Informe o primeiro valor:' ))
print('Selecione o operador desejaso')
print('1 Adição')
print('2 Subtração')
print('3 Multiplicação')
print('4 Divisão')
op = input('Informe a valor do operador desejado (1, 2, 3, 4): ')

if op == '1':
    res = v1 + v2
    print('---------------------------------')
    print(f'O resultado da adição é: {res}')
elif op == '2':
    res = v1 - v2
    print('---------------------------------')
    print(f'O resultado da subtração é: {res}')
elif op == '3':
    res = v1 * v2
    print('---------------------------------')
    print(f'O resultado da multiplicação é: {res}')
elif op == '4':
    if v2 != 0:
        res = v1 / v2
        print('---------------------------------')
        print(f'O resultado da divisão é: {res}')
    else:
        print('---------------------------------')
        print('Não é possivel dividir por zero.')
else:
    print('---------------------------------')
    print('Erro! Operador inválido.')
