# 1. O programa interage com o Noach
nome = input("Olá! Qual é o teu nome? ")
idade_texto = input(f"Prazer, {nome}! Quantos anos tens? ")

# 2. Conversão (Transformar texto em número)
idade = int(idade_texto)

# 3. A Tomada de Decisão
if idade >= 21:
    print(f"Muito bem, {nome}! Já és maior de idade e podes tirar a carta de"
          "condução. 🚗")
else:
    anos_que_faltam = 21 - idade
    print(f"Olha, {nome}, ainda és menor. Faltam {anos_que_faltam} anos para "
          "seres adulto! 🎮")
