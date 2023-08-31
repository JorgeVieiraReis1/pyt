# - Ler o nome de um aluno e os valores de quatro notas escolares. Calcular a média 
# aritmética e apresentar a mensagem “Aprovado” se a média obtida for maior ou igual 
# a 7; 
# Caso a média do aluno estiver abaixo de 4, o programa deve apresentar a mensagem 
# “Reprovado no Semestre”; 
# Caso a nota do aluno esteja entre 4 e 6,9 o programa deve solicitar a nota de exame 
# do aluno e calcular uma nova média aritmética entre a nota de exame com a primeira 
# média aritmética. Se o valor da nova média for maior ou igual a cinco apresentar a 
# mensagem “Aprovado em exame”; caso contrário, apresentar a mensagem 
# “Reprovado em exame”. 
# Informar junto com cada mensagem o valor da média obtida com os dados do aluno.

#Entrada

Nome = input('Digite seu nome:')
Nota1 = float(input("Nota1 = "))
Nota2 = float(input("Nota2 = "))
Nota3 = float(input("Nota3 = "))
Nota4 = float(input("Nota4 = "))

Media = (Nota1+Nota2+Nota3+Nota4)/4

if(Media >=7):
    print('\nAprovado | Média = %.2f' % Media)
elif(Media <4):
    print('\nReprovado no semestre')
else:
    Ne = float(input('Nota de exame NE ='))
    media2 = (Media + Ne)/2
    if (media2 >=5):
        print('Aprovado em exame | Média = %.2f'% media2)
    else:
        print('\nReprovado em exame |Média = %.2f'% Media)
    sair= ('\n Tecle enter para sair...')












 