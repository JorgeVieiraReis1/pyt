'''
- Efetuar o cálculo e a apresentação do valor de uma prestação em 
atraso, utilizando a fórmula: 
PRESTAÇÃO=VALOR+(VALOR*(TAXA/100)*TEMPO).
'''

"Entrada de dados"

entradaDeValor= input("insira o valor")
entradaDeTempo= input("insira o tempo em meses")
entradaDeTaxa= input("insira a taxa")

"Processo"

entradaDeValor= float(entradaDeValor.replace(',','.'))
entradaDeTempo= int(entradaDeTempo)
entradaDeTaxa= float(entradaDeTaxa.replace(',','.'))/100
prestação= entradaDeValor+(entradaDeValor*entradaDeTaxa)*entradaDeTempo

"Saida de dados"

print( "o calculo da prestação em atraso foi de ",f'{prestação:.4f}' )
