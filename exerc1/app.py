#*************************************************************************************************************************
#Objetivo: Realizar a entrada do nome e 4 notas escolares de um aluno e apresentar a media e o status de aprovação do aluno
#Data:21/08/2023
#Autor:Jorge
#Versão:2.0
#****************************************************************************************************************

#Entrada de dados
nome = input('Digite o nome do aluno ')
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

#versão2.0
# if(media>=7):
#     if(frequencia>= 75):
#         print("A media do aluno", nome, 'foi:', media)
#         print('o aluno está APROVADO.')
#     else:
#         print('Aluno REPROVADO POR FREQUENCIA')
# else:
#         print("A media do aluno", nome, 'foi:', media)
#         print('o aluno está REAPROVADO por nota.')

#versão 2.1
# if (media>= 7 and frequencia >=75):
#     print('A media do aluno', nome'foi:',media)
#     print('o aluno está APROVADO')
# else:
#     print('A media do aluno',nome,'foi:'media)
#     print('A frequencia do aluno', nome'foi:',frequencia,'%')
#     print('o aluno está REPROVADO.')
           
#veresão 2.2
if(nota1 <0 or nota1 >10 or nota2 <0 or nota2>10 or nota3 <0 or nota3 >10 or nota4 <0 or nota4 >10 or frequencia<0 or frequencia>100):
    print('ERRO: As notas digitadas devem estar ENTRE 0 E 10, JÁ A FEQUENCIA DEVE ESTAR ENTRE 0 E 100.')
if (media>=7 and frequencia >=75):
    print('A media do aluno',nome,'foi:',media)
    print('o aluno está APROVADO')
else:
    print('A media do aluno',nome,'foi:',media)
    print('A frequencia do aluno',nome,'foi:',frequencia,'%')
    print('o aluno está REPROVADO.')
           

