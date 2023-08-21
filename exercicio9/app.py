#******************************************************************
#Objetivo: Realizar a conversão e graus Celsius para F...
#14/08/2023





#Entrada de dados
celsius = input('Digite o valor em graus Celsius a ser convertido')

#Processamento
#convertendo para numero real e tratando a entrada e da ","
celsius = float(celsius.replace(',','.'))
fahrenheit = (9*celsius+160)/5


#Saída de dados
print ('o valor convertido é :'fahrenheit, 'ºF')
