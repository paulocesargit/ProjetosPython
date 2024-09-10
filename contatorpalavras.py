def contar_palavras(frase):
    palavras = frase.split()
    return len(palavras)

if __name__ == "__main__":
    frase = input("Digite uma frase ou parágrafo: ")
    print(f"O número de palavras é: {contar_palavras(frase)}")