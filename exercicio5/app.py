'''
- Ler quatro valores numéricos inteiros e apresentar o resultado das 
adições e das multiplicações utilizando a propriedade distributiva para 
máxima combinação possível entre quatro variáveis. Considerando-se 
o uso das variáveis A, B, C e D, devendo ser feita seis adições e seis 
multiplicações, ou seja, de forma geral deve ser combinada a variável 
A com a variável B, a variável A com a variável C, a variável A com a 
variável D. Depois será necessário combinar a variável B com a variável 
C e a variável B com a variável D e por fim a variável C será combinada 
com a variável D. 
'''
#Entrada de dados#
entradaVariavelA= int(input("Digite o primeiro valor"))
entradaVariavelB= int(input("Digite o segundo valor"))
entradaVariavelC= int(input("Digite o terceiro valor"))
entradaVariavelD= int(input("Digite o terceiro valor"))

#Processo#
#somas
somarAcomB= entradaVariavelA+entradaVariavelB
somarAcomC= entradaVariavelA+entradaVariavelC
somarAcomD= entradaVariavelA+entradaVariavelD
somarBcomC= entradaVariavelB+entradaVariavelC
somarCcomD= entradaVariavelC+entradaVariavelD
somarBcomD= entradaVariavelB+entradaVariavelD

#multiplicações
multiplicarAcomB= entradaVariavelA*entradaVariavelB
multiplicarAcomC= entradaVariavelA*entradaVariavelC
multiplicarAcomD= entradaVariavelA*entradaVariavelD
multiplicarBcomC= entradaVariavelB*entradaVariavelC
multiplicarCcomD= entradaVariavelC*entradaVariavelD
multiplicarBcomD= entradaVariavelB*entradaVariavelD

#saida de dados#
print