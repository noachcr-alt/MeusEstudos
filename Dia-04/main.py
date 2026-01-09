# O Noach define as informações
clima = "sim"
vento = "sim"

# Entrada de dados
resposta = input("Está chovendo? ")

if resposta == clima:  # True
    print("está chovendo!")

    # AGORA O IF DENTRO DO IF (Segunda camada de segurança)
    resp_vento = input("Está ventando muito forte? ")

    if resp_vento == vento:
        print("Então é melhor ficar em casa! ")
    else:
        print("Então é melhor levar o guarda-chuva! ")

else:  # False
    print("Pode ficar tranquila e ir ao parque! ")


salgado = "sim"
calabresa = "sim"

resp_salg = input("Tem salgado? ")

if resp_salg == salgado:  # True
    print("Ah que bom!")

    resp_calab = input("Você tem de calabresa? ")

    if resp_calab == calabresa:
        print("Então vou querer um!")
    else:
        print("Poxa que pena, obrigado entâo!")

else:  # False
    print("Ah que pena, mas muito obrigado!")
