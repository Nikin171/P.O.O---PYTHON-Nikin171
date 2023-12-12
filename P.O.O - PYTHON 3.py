#1 - Faça um programa que mostre a mensagem "alo mundo":
'''
print('Olá Mundo!!')
'''
#2 - Faça um programa que peça um numero e então mostre a mensagem,o numero informado foi {numero}
'''
n = int(input(f'Digite um numero: '))
print(f'O numero informado foi:', n)
'''
#3 - Faça um programa que peça 2 numeros imprima a soma:
'''
n1 = int(input(f'Digite o primeiro número: '))
n2 = int(input(f'Digite o segundo número: '))
soma = n1 + n2
print('A soma dos números é:', n1 + n2)
'''
#4 - Faça um programa que peça as 4 notas bimestrais e mostre a media:
'''
n1 = float(input(f'Digite a primeiro nota: '))
n2 = float(input(f'Digite a segunda nota: '))
n3 = float(input(f'Digite a terceira nota: '))
n4 = float(input(f'Digite a quarta nota: '))
media = n1 + n2 + n3 + n4 / 4
print(f'A média das notas foram: ', media)
'''
#5 - Faça um programa que peça 2 numeros e imprima o maior deles:
'''
n1 = int(input(f'Digite o primeiro número: '))
n2 = int(input(f'Digite o segundo número: '))
if n1 > n2:
    print(f'O maior número é: ',n1)
if n1 < n2:
    print('O maior número é:',n2)
'''
#6 - Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo:
'''
n1 = int(input(f'Digite um número qualquer:'))
if n1 < 0:
    print(f'****Número é negativo seu arrombado.****')
if n1 >= 0:
    print(f'****O número é positivo seu bosta.****')
'''
#7 - Faça um programa que verifique se uma letra digitada é vogal ou consoante:
'''
letra = input(f'Digite uma letra qualquer: ')

if letra == letra == 'A' or letra =='a' or letra =='E' or letra =='e' or letra =='I' or letra =='i' or letra =='O' or letra =='o' or letra =='U' or letra =='u':
    print(f'***Essa letra é uma vogal***')

else:
    print(f'***Isso é uma consoante***')
'''
#8 - Faça um programa que peça um numero inteiro e determine se ele é par ou ímpar:
'''
n1 = int(input(f'Digite um número qualquer:'))

if n1 % 2 == 0:
    print('O número é par')
else:
    print('O número é ímpar')
'''
#9- Faça um programa, com uma função que necessite de tres argumentos e que forneça a soma desses tres argumentos.
'''
def soma_tres_argumentos(a, b, c):
    resultado = a + b + c
    return resultado

n1 = float(input(f'Digite o primeiro numero:'))
n2 = float(input(f'Digite o segundo numero:'))
n3 = float(input(f'Digite o terceiro numero:'))

resultado_soma = soma_tres_argumentos(n1, n2, n3)
print(f'A soma dos três números é: {resultado_soma}')
'''
#10- Faça uma função que informe a quantidade de digitos de um determinado numero inteiro informado.
'''
def contar_digitos(numero):
    qtd_digitos = len(str(numero))
    return qtd_digitos
numero_informado = int(input('Digite um número inteiro: '))
quantidade_digitos = contar_digitos(numero_informado)
print(f'O número {numero_informado} tem {quantidade_digitos} dígitos.')
'''
#11- Data com mes por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no format de dia,mes e ano por extenso. Opcionalmente, valide a data e retorne NULL caso a data seja invalida.

# 1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos. 
'''
def soma_3_argumentos(a,b,c):
    resultado = a+b+c
    return resultado
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

resultado_soma = soma_3_argumentos(n1,n2,n3)
print(f'A soma dos três números é: {resultado_soma}')
'''
# 2. Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado. 
'''
def contar_digitos(numero):
    qtd_digitos = len(str(numero))
    return qtd_digitos

numero_informado = int(input('Digite um número inteiro: '))
qtd_digitos_resultado = contar_digitos(numero_informado)

print(f'O número {numero_informado} possui {qtd_digitos_resultado} dígitos!!')
'''
# 3.Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
'''
from datetime import datetime

def data_por_extenso(data_str):
    try:
        data_obj = datetime.strptime(data_str,'%d/%m/%y')

        data_extenso = data_obj.strftime('%d de %B de %y')

        return data_extenso
    
    except ValueError:
        print('Data Inválida. Retornando NULL.')
        return None
    
data_input = input('Digite uma data no formato DD/MM/AAAA: ')

data_extenso_resultado = data_por_extenso(data_input)

if data_extenso_resultado is not None:
    print(f'A data por extenso é: {data_por_extenso}')
else:
    print(f'Data Inválida. Resultado: NULL')
'''
# 4.Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
'''
def comparar_strings(str1, str2):
    # Exibindo o conteúdo das strings
    print(f"Conteúdo da primeira string: {str1}")
    print(f"Conteúdo da segunda string: {str2}")

    # Obtendo e exibindo o comprimento das strings
    len_str1 = len(str1)
    len_str2 = len(str2)
    print(f"Comprimento da primeira string: {len_str1}")
    print(f"Comprimento da segunda string: {len_str2}")

    # Verificando se as strings têm o mesmo comprimento
    if len_str1 == len_str2:
        print("As strings têm o mesmo comprimento.")

        # Verificando se as strings são iguais
        if str1 == str2:
            print("As strings são iguais.")
        else:
            print("As strings são diferentes.")
    else:
        print("As strings têm comprimentos diferentes.")

# Exemplo de uso da função
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

comparar_strings(string1, string2)
'''
