def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def menu():
    print("Escolha uma conversão de temperatura:")
    print("1. Celsius para Fahrenheit")
    print("2. Celsius para Kelvin")
    print("3. Fahrenheit para Celsius")
    print("4. Kelvin para Celsius")

    escolha = int(input("Digite o número da conversão desejada: "))

    if escolha == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"Temperatura em Fahrenheit: {celsius_para_fahrenheit(celsius)}")
    elif escolha == 2:
        celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"Temperatura em Kelvin: {celsius_para_kelvin(celsius)}")
    elif escolha == 3:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"Temperatura em Celsius: {fahrenheit_para_celsius(fahrenheit)}")
    elif escolha == 4:
        kelvin = float(input("Digite a temperatura em Kelvin: "))
        print(f"Temperatura em Celsius: {kelvin_para_celsius(kelvin)}")
    else:
        print("Escolha inválida!")

if __name__ == "__main__":
    menu()