class Pessoas:
    
    def __init__(self,nome,sobrenome,cpf,):
        self.nome=nome
        self.sobrenome=sobrenome
        self.cpf=cpf
       
    def nome_completo():
       return '{self.nome} {self.sobrenome}'


class Cliente(Pessoas):
    
    def __init__(self,nome,sobrenome,cpf,renda):
        Pessoas.__init__(self,nome,sobrenome,cpf)
        self.renda=renda
        
    def nome_completo(self): 
       return f'Nome_Cliente: {self.nome} {self.sobrenome} {self.renda}'
   
class Funcionario(Pessoas):
    
    def __init__(self,nome,sobrenome,cpf,matricula):
        Pessoas.__init__(self,nome,sobrenome,cpf)
        self.matricula=matricula
        
    def nome_completo(self):
        return f'Nome_Funcionario: {self.nome} {self.sobrenome}'
        
Cliente1=Cliente("Paulo","Cesar",15673772747,15.000) 
funcionario1=Funcionario('Ana','Oliveira',52563626623,873727)
print(Cliente1.nome_completo())
print(funcionario1.nome_completo())


    
