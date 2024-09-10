contatos = {}

def adicionar_contato(nome, telefone):
    contatos[nome] = telefone
    print(f"Contato {nome} adicionado com sucesso.")

def editar_contato(nome, telefone):
    if nome in contatos:
        contatos[nome] = telefone
        print(f"Contato {nome} atualizado.")
    else:
        print(f"Contato {nome} não encontrado.")

def excluir_contato(nome):
    if nome in contatos:
        del contatos[nome]
        print(f"Contato {nome} excluído.")
    else:
        print(f"Contato {nome} não encontrado.")

def mostrar_contatos():
    if contatos:
        for nome, telefone in contatos.items():
            print(f"Nome: {nome}, Telefone: {telefone}")
    else:
        print("Nenhum contato encontrado.")