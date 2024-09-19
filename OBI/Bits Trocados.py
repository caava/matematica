c = 50  # cédulas de 50
d = 10  # cédulas de 10
s = 5   # cédulas de 5
u = 1   # cédulas de 1

testes = []  # Para armazenar os resultados de cada teste

while True:
    V = int(input('Informe o valor solicitado para o saque: '))  # Solicita o valor do saque
    if V == 0:  # Se o valor for 0, encerra o loop
        break
    
    saque = []  # Armazena a quantidade de cédulas para esse saque
    
    saque.append(V // c)  # Calcula o número de cédulas de 50 e adiciona à lista
    V = V % c  # Atualiza o valor restante após usar as cédulas de 50
    
    saque.append(V // d)  # Calcula o número de cédulas de 10 e adiciona à lista
    V = V % d  # Atualiza o valor restante após usar as cédulas de 10
    
    saque.append(V // s)  # Calcula o número de cédulas de 5 e adiciona à lista
    V = V % s  # Atualiza o valor restante após usar as cédulas de 5
    
    saque.append(V // u)  # Calcula o número de cédulas de 1 e adiciona à lista
    V = V % u  # Atualiza o valor restante após usar as cédulas de 1 (deve ser 0)
    
    testes.append(saque)  # Armazena o resultado deste saque na lista de testes

# Exibe os resultados no formato solicitado
for i, resultado in enumerate(testes):  # Itera sobre a lista de testes, exibindo os resultados
    print(f"Teste {i+1}")  # Imprime o número do teste
    print(f"{resultado[0]} {resultado[1]} {resultado[2]} {resultado[3]}\n")  # Imprime o resultado formatado do saque
