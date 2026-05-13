# Compreendendo laços
clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]
for cliente in clientes:
    print(f"Olá, {cliente}! Bem-vindo(a) à nossa loja!")

# Quantas vezes a mensagem será exibida?
quantidade = 5
for i in range(quantidade):
    print("Bem vindo ao buscante.")

# Calculando a soma de números
valores = [10, 20, 30, 40, 50]
soma = 0
for valor in valores:
    soma += valor
print(f"A soma das receitas é: {soma}")

# Organizando portfolio
projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]
for projeto in projetos:
    if projeto is not None:
        print(f"Projeto: {projeto}")
    else:
        print("Projeto ausente!")

# Usando o break
livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]
for livro in livros:
    if livro == "O Hobbit":
        print("Livro encontrado!")
        break
    print(f"Verificando o livro: {livro}")