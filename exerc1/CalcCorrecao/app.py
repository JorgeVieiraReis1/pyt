# sistema de uma calculadora
# 1-	2 entradas de valores
# 2-	1 entrada de operação 
# Soma, subtração, multiplicação e divisão( Escolher uma dessas).
# Validações
# Valores Vazios.
# Somente aceita essas operações.
# Não existe divisões por zero
# Tratamento da vírgula(replace)

#*************************************************************************************************************************
#Objetivo: Criar um sistema de calculadora utilizando uma das operações aritméticas
#Data:22/08/2023
#Autor:Jorge
#Versão:1.0
#****************************************************************************************************************
#Entrada
valor1= float(input('Digite o valor1:'))
valor2= float(input('Digite o valor2:'))
operacao = input('Escolha a operação desejada[SOMAR|SUBTRAIR|DIVIDIR|MULTIPLICAR]:')
operacao = ('')
#Processo
# UPPER()- CONVERTE O CONTEUDO DE UMA STRING EM MAIUSCULO
# LOWER()- CONVERTE O CONTEUDO DE UMA STRING EM MINUSCULO
#Convertendo as variaveis de String para Float

if(valor1.is numeric()== 'false'or valor2.isnumeric()=='false'):
valor1= float(valor1.replace(',','.'))
valor2= float(valor2.replace(',','.'))

if(valor1 == ''or valor2 ==)
if(operacao.upper() =='SOMAR'):
    resultado= valor1 + valor2
else:
    if(operacao.upper() == 'SUBTRAIR'):
        resultado= valor1 - valor2
    else:
        if(operacao.upper() == 'DIVIDIR'):
            if(valor2 ==0):
                print('Erro: Não existe divisão por 0.')
        else: 
            if(operacao.upper() == 'Multiplicar'):
                resultado = valor1 * valor2
            else:
                print('Erro:Operação escolhida é inválida.')
print (resultado)
