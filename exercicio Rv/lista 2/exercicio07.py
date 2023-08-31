#*************************************************************************************************************************
#Objetivo: Programa que Leia três valores e apresentá-los dispostos em ordem crescente.
#Data:31/08/2023
#Autor:Jorge
#Versão:1.0
#***************************************************************************************************************************


v1= int(input("Digite o primeiro valor:"))
v2 = int(input("Digite o segundo valor:"))
v3 = int(input("Digite o terceiro valor:"))

if(v1 < v2 and v2 < v3):
    print(f'A ordem crescente é {v1} , {v2} e {v3}')
elif v1 > v2 and v1 >v3 and v3 < v2:
    print(f'A ordem crescente é {v1} , {v3} e {v2}')
elif v2 < v1 and v2 > v3 and v1 > v3:
    print(f'A ordem crescente é {v2} , {v1} e {v3}')
elif v2 < v1 and v1 > v3 and v3 < v1:
    print(f'A ordem crescente é {v2} , {v3} e {v1}')
elif v3 < v1 and v3 < v2 and v1 > v2:
    print(f'A ordem crescente é {v3} , {v1} e {v2}')
elif v3 < v2 and v2 < v1:
    print(f'A ordem crescente é {v3} , {v2} e {v1}')
else:
    print('erro')