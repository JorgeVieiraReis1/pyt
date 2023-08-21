#*************************************************************************************************************************
#Objetivo: Realizar a entrada do nome e 4 notas escolares de um aluno e apresentar a media e o status de aprovação do aluno
#Data:21/08/2023
#Autor:Jorge
#Versão:2.0
#****************************************************************************************************************

#Entrada de dados
nome = input('Digite o nome do aluno')
nota1= float(input('Digite a nota1:'))
nota2= float(input('Digite a nota2:'))
nota3= float(input('Digite a nota3:'))
nota4= float(input('Digite a nota4:'))
frequencia = int(input('Digite a frequencia do aluno'))

#Processo
media= (nota1+ nota2+nota3+nota4)/4

# if(media>=7):
#     print('A media do aluno',nome, 'foi:',media)
#     print('O aluno está APROVADO.')
# else:
#      print('A media do aluno',nome, 'foi:',media)
#      print('O aluno está REPROVADO.')

if(media>=7):
    if(frequencia>= 75):
        print("A media do aluno", nome, 'foi:', media)
        print('o aluno está APROVADO.')
    else:
        print('Aluno REPROVADO POR FREQUENCIA')
else:
        print("A media do aluno", nome, 'foi:', media)
        print('o aluno está REAPROVADO por nota.')



