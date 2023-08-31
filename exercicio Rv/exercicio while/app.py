# ***********************************************************************************************************************************************
# Objetivo: realizar estrutura de repetição utilizando o While
#Data: 31/08/2023
#Autor: Jorge
#Versão: 1.0
# **********************************************************************************************************************************************
valorminimo = int(input('Digite o numero inicial da sequencia de valores'))
valormaximo = int(input('Digite o maximo de valor que deseja exibir:'))
contador = valorminimo
while (contador<= valormaximo):
    if(contador%2 == 0):
        print('O numero', contador,'é par' )
    else:
        print('O numero:',contador, 'é ímpar')
    contador = contador +1 
      
