# --- DEFINIÇÃO DA FUNÇÃO ---
def verificar_portaria(
    nome_motorista: str, horario_atual: int, possui_cracha: bool
):
    print("--- Sistema de Segurança Noach ---")
    print(f"Olá {nome_motorista}")
    # Primeiro nível de decisão (Horário)
    if horario_atual < 18:
        print("Está dentro do horário de funcionamento...")

        # Segundo nível (IF Aninhado - Crachá)
        if possui_cracha:
            print("Status: Acesso LIBERADO! 🟢")
        else:
            print("Status: Acesso NEGADO! Sem crachá. 🔴")

    else:
        # Resposta caso o primeiro IF seja falso (Horário > 18)
        print("Status: Portaria FECHADA! 🌙")


# --- CHAMANDO A FUNÇÃO PARA ELA FUNCIONAR ---
verificar_portaria("Pedro", 17, False)
verificar_portaria("Marcos", 19, True)
verificar_portaria("João", 14, False)
