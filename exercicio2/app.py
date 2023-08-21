'''Calcular e apresentar o valor do volume de uma lata de óleo, 
utilizando a fórmula: VOLUME=3.14159*R^2*ALTURA.'''

#Entrada de dados
entradaDoRaio = input('digite o raio da lata')
entradaDaAltura = input('digite a altura da lata')

#processamento
raio = float(entradaDoRaio.replace(',','.'))
altura = float(entradaDaAltura.replace(',','.'))

volume = 3.14159*raio**2*altura


#saida de dados
print('o volume da lata é',f'{volume:_.4f}','cm³')