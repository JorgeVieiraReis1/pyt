#*************************************************************************************************************************
#Objetivo: Programa que faça o cálculo do IMC.
#Data:31/08/2023
#Autor:Jorge
#Versão:1.0
#***************************************************************************************************************************
# Um consultório de Nutrição solicitou a você que criasse um sistema que faça o
# cálculo do IMC de uma pessoa, você deve pesquisar a fórmula e as condições do IMC
# para criar o sistema.

altura = float(input('Entre com sua altura:').replace(',','.'))   
peso = float(input('Entre com seu peso:'))  

imc = peso/(altura * altura)  
print('Seu índice de massa corporal é {:.2f}'.format(imc))  