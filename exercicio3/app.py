"""
Efetuar o cálculo da quantidade de litros de combustível gasta em 
uma viagem, utilizando um automóvel que faz 12 km por litro. Para 
obter o cálculo, o usuário deve fornecer o tempo gasto e a velocidade 
média percorrida durante viagem. Desta forma, será possível obter a 
distância percorrida com a fórmula DISTÂNCIA=TEMPO*VELOCIDADE. 
Tendo o valor da distância, basta calcular a quantidade de litros usados 
de combustível utilizada na viagem com a fórmula: 
LITROS_USADOS=DISTÂNCIA/12. O programa deve apresentar os 
valores da velocidade média, tempo gasto na viagem, à distância 
percorrida e a quantidade de litros utilizada na viagem.
"""
#Entrada de dados#
EntradaDaVelocidade = int(input('Digite a velocidade em Km/h'))
EntradaDoTempo = input('Digite o tempo em minutos')
EntradaDoConsumo = input('Digite o consumo em combustível')

#Processamento#
EntradaDoConsumo = float(EntradaDoConsumo.replace(',','.'))
EntradaDoTempo = float(EntradaDoTempo)/60
EntradaDaDistancia = EntradaDoTempo*EntradaDaVelocidade
LitrosUsados=EntradaDoConsumo*EntradaDaDistancia

#Saida de dados#
print('Um carro com velocidade media de ',EntradaDaVelocidade ,'km/h, por',EntradaDoTempo ,'minutos, em uma distancia de',EntradaDaDistancia, 'km, consumiria', EntradaDoConsumo,'L' )


