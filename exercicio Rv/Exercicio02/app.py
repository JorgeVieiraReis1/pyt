# - Ler o nome e o sexo de uma pessoa e apresentar como saída uma das seguintes 
# mensagens: “Ilmo. Sr.”, caso seja informado o sexo como masculino ou “Ilma. Sra.”, 
# caso seja informado o sexo como feminino. Apresentar também junto com cada 
# mensagem de saudação o nome previamente informado. 
# Ex: “Bem-vindo Ilmo. Sr. José”

#entrada
nome = input("Digite seu nome")
sexo = input("Digite o seu sexo, f(feminino)m(masculino):")

#Processo
if(sexo == 'm'):
    print ('Bem-vindo Ilmo. Sr.', nome)
elif(sexo == 'f'):
    print ('Ilma. Sra.', nome)
else:
    print('Erro, opção inválida, digite f ou m') 
















