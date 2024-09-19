N = 1
contador = 1

lista = []
testes = []

while N != 0:
    N = int(input("Número de participantes da festa: ")) # Declaração da variável número de participantes
    ingresso = input("Informe a ordem de entrada: ")
    lista = ingresso.split()
    if contador == N:
        for i in range(lista):
            if (i+1) == lista[i]:
                testes.append([f'Teste [{contador}]', {i + 1 }])

    contador+=1
