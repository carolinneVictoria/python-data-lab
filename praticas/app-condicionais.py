# Calculando total de frutas vendidas
macas = int(input("Digite a quantidade de maçãs vendidas: "))
bananas = int(input("Digite a quantidade de bananas vendidas: "))

if macas > bananas:
    print("A quantidade de maçãs vendidas é maior do que a quantidade de bananas vendidas.")
elif bananas > macas:
    print("A quantidade de bananas vendidas é maior do que a quantidade de maçãs vendidas.")
else:
    print("A quantidade de maçãs vendidas é igual à quantidade de bananas vendidas.")

# Calculando tempo de projeto
atvA = int(input("Informe os dias para a atividade A:"))
atvB = int(input("Informe os dias para a atividade B:"))
atvC = int(input("Informe os dias para a atividade C:"))

if atvA | atvB | atvC < 0:
    print("Erro: Os dias não podem ser negativos.")
else:
    tempo_total = atvA + atvB + atvC
    print(f"O tempo total do projeto é de {tempo_total} dias.")

# Temperatura dos servidores
temp_atual = int(input("Digite a temperatura atual: "))
if temp_atual > 25:
    print("Alerta! Temperatura acima do limite permitido!")
else:
    print("Temperatura dentro do limite seguro.")

# Calculando orçamento mensal
limite = 3000.0
despesas_mes = float(input("Digite o total de despesas do mês (R$): "))
if despesas_mes > limite:
    print("Atenção! Você ultrapassou o limite do orçamento!")
else:
    print("Ótimo! Você está dentro do orçamento mensal.")