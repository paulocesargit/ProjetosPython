valor_da_casa = float(input("Digite o valor da casa: "))
salário_usuario = float(input("Digite o salário: "))
anos = int(input("Quantos anos para pagar: "))
meses = anos * 12
prestacao = valor_da_casa / meses
if prestacao > salário_usuario * 0.3:
    print("Infelizmente você não pode obter o empréstimo")
else:
    print(f"Valor da prestação: R$ {prestacao:7.2f} Empréstimo OK")