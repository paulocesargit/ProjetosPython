velocidade = float(input("Digite a velocidade percorrida em km: "))

if velocidade <= 80:
   print(f"Sem multas a pagar ")
else:
    multa = 5.0   
    preco_a_pagar = velocidade * multa
    print(f"O valor da Multa é: R$ {preco_a_pagar:.2f}")