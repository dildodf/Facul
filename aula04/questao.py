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
        if idade == 16:
            print('Opcional.')
        else:
            if idade == 17:
                print('Opcional.')
            else:
                if idade == 37:
                    print('Ganha pêmio e não vota.')
                else:
                    if idade > 60:
                        print('O voto é opcional.')
                    else:
                        if idade == 74:
                            print('O voto é obrigatório, no entanto recebe prêmio')
                        else:
                            print('O voto é obrigatório')

#Forma 2
'''
def verificar_idade(idade):
    if idade < 0:
        return "não nasceu"
    else:
        if idade < 16:
            return "não vota"
        else:
            if idade == 16:
                return "voto opcional"
            else:
                if idade == 17:
                    return "voto opcional"
                else:
                    if idade == 37:
                        return "ganha prêmio e não vota"
                    else:
                        if idade > 60:
                            return "voto opcional"
                        else:
                            if idade == 74:
                                return "voto obrigatório, no entanto recebe prêmio"
                            else:  # idade > 17
                                return "voto obrigatório"

# Solicita a idade do usuário
idade_input = int(input("Digite a idade do cidadão: "))
resultado = verificar_idade(idade_input)
print(resultado)
'''
