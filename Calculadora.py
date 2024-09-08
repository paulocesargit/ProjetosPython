while True:
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input('Escolha o operador: [+], [-], [*] ou [/]: ')

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)

        if operador == '+':
            resultado = numero_1_float + numero_2_float
            print(f'{numero_1} + {numero_2} = {resultado:.2f}')

        elif operador == '-':
            resultado = numero_1_float - numero_2_float
            print(f'{numero_1} - {numero_2} = {resultado:.2f}')

        elif operador == '*':
            resultado = numero_1_float * numero_2_float
            print(f'{numero_1} * {numero_2} = {resultado:.2f}')

        elif operador == '/':
            if numero_2_float != 0:
                resultado = numero_1_float / numero_2_float
                print(f'{numero_1} / {numero_2} = {resultado:.2f}')
            else:
                print('Não é possível dividir por zero.')

        else:
            print('Operador inválido.')

    except ValueError:
        print('Entrada inválida. Por favor, insira números válidos.')

    sair = input('Você deseja [S]sair? ').lower().startswith('s')
    if sair:
        print('Você saiu')
        break
