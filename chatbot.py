def responder_entrada(usuario_entrada):
    usuario_entrada = usuario_entrada.lower()
    
    if "olá" in usuario_entrada or "oi" in usuario_entrada:
        return "Olá! Como posso ajudá-lo hoje?"
    elif "como você está" in usuario_entrada:
        return "Estou funcionando perfeitamente!"
    elif "tchau" in usuario_entrada or "adeus" in usuario_entrada:
        return "Tchau! Tenha um ótimo dia!"
    else:
        return "Desculpe, não entendi. Pode reformular sua pergunta?"

def chatbot():
    print("Bem-vindo ao Chatbot! Digite 'sair'para encerrar.")
    
    while True:
        usuario_entrada = input("Você: ")
        if usuario_entrada.lower() == "sair":
            print("Chatbot: Até logo!")
            break
        
        resposta = responder_entrada(usuario_entrada)
        print(f"Chatbot: {resposta}")