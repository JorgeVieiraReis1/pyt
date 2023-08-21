






## entrada de dados

nome = input('Digite o nome do aluno:')
nota1 = input('Digite a nota1:')
nota2= input('Digite a nota2:')
nota3 = input('Digite a nota3:')
nota4 = input('Digite a nota4:')

#processamento
#replace - permite localizar um caracter e substituir po outro
nota1 = float(nota1.replace(',','.'))
nota2 = float(nota2.replace(',','.'))
nota3 = float(nota3.replace(',','.'))
nota4 = float(nota4.replace(',','.'))
media = ( nota1 + nota2 +  nota3 +  nota4) /4

#Saida de dados
print ('A media final do aluno', nome, 'e', f'{media:_.1f}')