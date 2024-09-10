def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))
imc = calcular_imc(peso, altura)
categoria = interpretar_imc(imc)
print(f"Seu IMC é: {imc:.2f} ({categoria})")