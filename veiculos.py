class Carros : #criando a classe
    def __init__(self,nome,fabricante,cor,ano,placa): 
        self.nome=nome
        self.fabricante=fabricante
        self.cor=cor
        self.ano=ano
        self.placa=placa
        
    def info(self): 
        print(f"Nome:{self.nome}")
        print(f"Fabricante:{self.fabricante}")
        print(f"Cor:{self.cor}")
        print(f"Ano:{self.ano}")
        print(f"Placa:{self.placa}")
         
veiculo1=Carros("320i","bmw","White",2020,"PJK45456") 
veiculo1.info()
veiculo2=Carros("A3","Audi","Red",2022,"Gaf69553") 
veiculo2.info()

class Motos : 
    def __init__(self,nome,fabricante,cor,ano,placa): 
        self.nome=nome
        self.fabricante=fabricante
        self.cor=cor
        self.ano=ano
        self.placa=placa
        
    def info(self): 
        print(f"Nome:{self.nome}")
        print(f"Fabricante:{self.fabricante}")
        print(f"Cor:{self.cor}")
        print(f"Ano:{self.ano}")
        print(f"Placa:{self.placa}")

veiculo1=Motos("G23","bmw","Blu",2020,"LK035456") 
veiculo1.info()
veiculo2=Motos("cg","Honda","Red",2018,"DR369553") 
veiculo2.info()
