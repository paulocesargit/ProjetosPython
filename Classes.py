class Cliente : 
    def __init__(self,nome,sobrenome,cpf,renda): 
        self.nome=nome
        self.sobrenome=sobrenome
        self.cpf=cpf
        self.renda=renda
        
    def info(self): 
        print(f"Nome:{self.nome}")
        print(f"Fabricante:{self.sobrenome}")
        print(f"Cor:{self.cpf}")
        print(f"Ano:{self.renda}")
         
Cliente1=Cliente("Paulo","Cesar",15673772747,15.000,) 
Cliente1.info()
Cliente2=Cliente("Matheus","Felipe",54573782857,15.000,) 
Cliente2.info()
Cliente2=Cliente("Bruno","Dornelas",54573782857,15.000,) 
Cliente2.info()

class Funcionarios : 
    def __init__(self,nome,sobrenome,cpf,matricula): 
        self.nome=nome
        self.sobrenome=sobrenome
        self.cpf=cpf
        self.matricula=matricula
        
    def info(self): 
        print(f"Nome:{self.nome}")
        print(f"Fabricante:{self.sobrenome}")
        print(f"Cor:{self.cpf}")
        print(f"Ano:{self.matricula}")
         
Cliente1=Funcionarios("Victor","Roma",15673772747,32323232,) 
Cliente1.info()
Cliente2=Funcionarios("Marillya","kattylun",54573782857,2243434343,) 
Cliente2.info()
Cliente2=Funcionarios("Tuios","Bernado",54573782857,3434343434,) 
Cliente2.info()