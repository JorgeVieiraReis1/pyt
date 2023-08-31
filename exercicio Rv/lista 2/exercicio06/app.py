# Ler cinco valores numéricos inteiros, identificar e apresentar o maior e o menor 
# valor informado. Não execute a ordenação dos valores.

#Entrada
valor1= int(input('Digite um valor inteiro'))
valor2= int(input('Digite um valor inteiro'))
valor3= int(input('Digite um valor inteiro'))
valor4= int(input('Digite um valor inteiro'))
valor5= int(input('Digite um valor inteiro'))

#Processo
if (valor1 < valor2):
    if (valor1 < valor3):
        if (valor1 < valor4):
            if(valor1 < valor5):
                print("\nMenor valor: %d" % valor1)
 
    if (valor2 < valor1):
        if (valor2 < valor3):
            if (valor2 < valor4):
                if(valor2 < valor5):
                    print("\nMenor valor: %d" % valor2)
                
    if (valor3 < valor1):
        if (valor3 < valor2):
            if (valor3 < valor4):
                if(valor3 <valor5):
                    print("\nMenor valor: %d" % valor3) 
                
    if (valor4 < valor1):
        if (valor4 < valor2):
            if (valor4 < valor3):
                if(valor4 < valor5):
                    print("\nMenor valor: %d" % valor4)     

    if (valor5 < valor1):
        if (valor5 < valor2):
            if (valor5 < valor3):
                if(valor5 < valor4):
                    print("\nMenor valor: %d" % valor5) 
    
    # Maior valor
    
    if (valor1 > valor2):
        if (valor1 > valor3):
            if (valor1 > valor4):
                if (valor1 > valor5):
                    print("\nMaior valor: %d" % valor1)
    
    if (valor2 > valor1):
        if (valor2 > valor3):
            if (valor2 > valor4):
                if (valor2 > valor5):
                    print("\nMaior valor: %d" % valor2)
                
    if (valor3 > valor1):
        if (valor3 > valor2):
            if (valor3 > valor4):
                if (valor3 > valor5):
                    print("\nMaior valor: %d" % valor3) 
                
    if (valor4 > valor1):
        if (valor4 > valor2):
            if (valor4 > valor3):
                if (valor4 > valor5):
                    print("\nMaior valor: %d" % valor4)

    if (valor5 > valor1):
        if (valor5 > valor2):
            if (valor5 > valor5):
                if (valor5 > valor4):
                    print("\nMaior valor: %d" % valor5)