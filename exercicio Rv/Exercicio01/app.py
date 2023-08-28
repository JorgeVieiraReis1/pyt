#comentario
# Ler dois valores numéricos inteiro e apresentar o resultado da diferença do maior 
# valor pelo menor valor

print('-apresentar o resultado da diferença do maior  valor pelo menor valor')

#exibe uma mensagem na tela

valor1 = int(input('digite o primeiro numero:'))
# solicitar a entrada de um valor para o ususario
valor2=int(input('digite o segundo numero:'))



maior = valor1
if(valor2> valor1) :
    resultado= valor2-valor1
    maior = valor2
else:
    resultado= valor1-valor2
    maior = valor1
#saida dos dados                    
print(f"O resultado maior valor digitado foi {maior}:")


