# Uma lista de preços de diferentes produtos
lista_precos = [10.0, 25.5, 50.0, 100.0]

# Aplicando um reajuste de 10% em cada preço automaticamente
for preco in lista_precos:
    preco_reajustado = preco * 1.10
    print("Preço antigo:", preco, "-> Novo preço com reajuste:", preco_reajustado)