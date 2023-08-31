

#Entrada de dados
tabuada = int(input('Escolha uma tabuada'))
valormaximo = int(input('Digite o maximo de valor que deseja exibir:'))
#Processamento
contador = 0
while(contador <= valormaximo):
    resultado = tabuada * contador
    print(tabuada, 'X', contador, '=', resultado)
    contador = contador +1