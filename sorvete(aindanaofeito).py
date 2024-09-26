p = int(input('Indique a largura em metros da praia: '))
s = int(input('Indique o numero de sorveteiros: '))

lista = []


for i in range(s):
     n1 = int(input(f"Insera o minimo de metros ocupados pela {i+1} sorveteria: "))
     lista.append(n1)
     n2 = int(input(f"Insera o maximo de metros ocupados pela {i+1} sorveteria: "))
     lista.append(n2)

     operacao = p - (n1 + n2) 

     
     
print(operacao)
''''  
if p == 0 and s == 0:
    print
'''
