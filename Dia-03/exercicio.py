nome = input("Olá! Qual é o teu nome? ")
saldo_texto = input(f"Prazer, {nome}! Qual é o seu saldo? ")

saldo = float(saldo_texto)

produto_texto = input("Qual o preço do produto? ")

produto = float(produto_texto)

resultado = saldo - produto

if resultado >= 0:
    print(f"Muito bem, {nome}! Você consegue comprar seu produto.")
    if resultado > 100:
        print("Como o que sobrou você pode usar para investir em algo.")
else:
    dinheiro_falta = produto - saldo
    print(f"Olha, {nome}, ainda falta dinheiro. Faltam R${dinheiro_falta:.2f} "
          "reais para comprar o produto!")
