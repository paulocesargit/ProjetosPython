nota01=float(input("Digite a nota de matematica : "))
nota02=float(input("Digite a nota de matematica : "))
nota03=float(input("Digite a nota de matematica : "))

nota04=float(input("Digite a nota de portugues : "))
nota05=float(input("Digite a nota de portugues : "))
nota06=float(input("Digite a nota de portugues : "))

nota07=float(input("Digite a nota de ciencia : "))
nota08=float(input("Digite a nota de ciencia : "))
nota09=float(input("Digite a nota de ciencia : "))

mediaportugues = (nota01 + nota02 + nota03 )/3
mediamatematica = (nota04 + nota05 + nota06 )/3
mediaciencia = (nota07 + nota08 + nota09 )/3

print("A nota do 1º Bimestre em matematica é: ",nota01)
print("A nota do 2º Bimestre em matematica é: ",nota02)
print("A nota do 3º Bimestre em matematica é: ",nota03)
print("A média final é: ",mediaportugues)

print("A nota do 1º Bimestre portugues é: ",nota04)
print("A nota do 2º Bimestre portugues é: ",nota05)
print("A nota do 3º Bimestre portugues é: ",nota06)
print("A média final é: ",mediamatematica)

print("A nota do 1º Bimestre em ciencias é: ",nota07)
print("A nota do 2º Bimestre em ciencias é: ",nota08)
print("A nota do 3º Bimestre em ciencias é: ",nota09)
print("A média final é: ",mediaciencia)


if mediamatematica >= 7:
  print("Aprovado")
elif mediamatematica <7 and mediamatematica >=5:
  print("Recuperaçao")
else:
  print("Não Aprovado")

if mediaportugues >= 7:
  print("Aprovado")
elif mediaportugues <7 and mediaportugues >=5:
  print("Recuperaçao")
else:
  print("Não Aprovado")

if mediaciencia >= 7:
  print("Aprovado")
elif mediaciencia <7 and mediaciencia >=5:
  print("Recuperaçao")
else:
  print("Não Aprovado")