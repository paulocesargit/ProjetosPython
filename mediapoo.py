class Aluno():
    def __init__(self, nome):
        self.nome = nome

    def calcular_media(self, nota1, nota2):
        return (nota1 + nota2) / 2

    def avaliar(self, media):
        if media >= 7.0:
            print(f'O aluno {self.nome} está \033[1;32;42m Aprovado! \033[m')
        elif 5.0 <= media < 7.0:
            print(f'O aluno {self.nome} está de \033[1;33;43m Recuperação \033[m')
        else:
            print(f'O aluno {self.nome} está \033[1;31;41m Reprovado \033[m')


nome_aluno = input("Digite o nome do aluno: ")
aluno = Aluno(nome_aluno)

nota01 = float(input("Digite a nota 1: "))
nota02 = float(input("Digite a nota 2: "))

media = aluno.calcular_media(nota01, nota02)
aluno.avaliar(media)

        