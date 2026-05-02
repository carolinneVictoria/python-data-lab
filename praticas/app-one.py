# ============================================================
# COLETA E AMOSTRAGEM DE DADOS
# ============================================================
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
soma = a + b
print(f"A soma de {a} e {b} é: {soma}")

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
soma = a + b + c
print(f"A soma de {a}, {b} e {c} é: {soma}")

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
subtracao = a - b
print(f"A subtração de {a} pelo {b} é: {subtracao}")

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
multiplicacao = a * b
print(f"A multiplicação de {a} por {b} é: {multiplicacao}")

# ============================================================
# COLETA E AMOSTRAGEM DE DADOS 2
# ============================================================
gastosEmpresa = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
totalGastos = sum(gastosEmpresa)
mediaGastos = totalGastos / len(gastosEmpresa)
print(f"Total de gastos: R$ {totalGastos:.2f}")
print(f"Média de gastos: R$ {mediaGastos:.2f}")

#2) Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.
comprasAcima3000 = [gasto for gasto in gastosEmpresa if gasto > 3000]
quantidadeComprasAcima3000 = len(comprasAcima3000)
porcentagemComprasAcima3000 = (quantidadeComprasAcima3000 / len(gastosEmpresa)) * 100
print(f"Quantidade de compras acima de R$ 3.000,00: {quantidadeComprasAcima3000}")
print(f"Porcentagem de compras acima de R$ 3.000,00: {porcentagemComprasAcima3000:.2f}%")

#3) Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].
numeros = []
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)
print("Lista de números inteiros:", numeros)