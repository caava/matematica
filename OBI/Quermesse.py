lista = []
testes = []

while True: # laço de repetição para uma quantidade indeterminada de testes
    N = int(input("Número de participantes da festa: ")) # declaração da variável número de participantes
    if N == 0: # caso a variável N for zero, o código para
        break
    ingresso = input("Informe a ordem de entrada: ") # declaração da ordem de entrada
    lista = ingresso.split() # manipulação da string ordem de entrada em uma lista com itens
    for i in range(len(lista)): # verificação do ganhador
        if int(lista[i]) == i+1:
            testes.append(lista[i]) # armazenamento do numero do bilhete ganhador

for i in range(len(testes)): # impressão dos testes informados
    print(f'Teste {i+1} \n{testes[i]}\n')