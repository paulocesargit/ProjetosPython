from tkinter import * 
from tkinter import ttk 
import sqlite3 

root = Tk()
 
class funcs(): 
    def limpa_cliente(self): 
        self.codigo_entry.delete(0, END) 
        self.nome_entry.delete(0, END) 
        self.telefone_entry.delete(0, END) 
        self.cidade_entry.delete(0, END),
 
 
    def conecta_db(self): 
        self.conn = sqlite3.connect("clientes_db") 
        self.cursor = self.conn.cursor();print("Conectado ao banco de dados") 
 
 
    def desconectar_db(self): 
        self.conn.close();print("Desconectado ao banco de dados") 
 
    def montartabela(self): 
        self.conecta_db() 
        # Criar Tabela 
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS clientes( 
                cod INTEGER PRIMARY KEY, 
                nome_cliente CHAR(60) NOT NULL, 
                telefone INTEGER(20), 
                cidade CHAR(40) 
                ); 
        """) 
        self.conn.commit()#comite para validar a conexão 
        self.desconectar_db()# Desconecta o banco de dados 
 
    def Variaveis(self):#essa função variaveis evita está repetidio as variaveis em outras funções 
 
        self.codigo = self.codigo_entry.get() 
        self.nome = self.nome_entry.get() 
        self.telefone = self.telefone_entry.get() 
        self.cidade = self.cidade_entry.get() 
 
    def add_cliente(self): 
        self.Variaveis() 
        self.conecta_db()#permite chamar o sqllite 
        # usamos aspa tripla caso seja necessario no banco 
        self.cursor.execute(""" INSERT INTO clientes(nome_cliente,telefone,cidade) 
            VALUES(?,?,?) """, (self.nome, self.telefone, self.cidade)) 
        self.conn.commit() 
        self.desconectar_db() 
        self.select_lista() 
        self.limpa_cliente() 
 
    def select_lista(self): 
        self.listaCli.delete(*self.listaCli.get_children()) 
        self.conecta_db() 
        lista=self.cursor.execute("""SELECT cod,nome_cliente,telefone,cidade FROM clientes 
            ORDER BY nome_cliente ASC;""")#o select classifica em ordem alfabetica(asc) 
 
        for i in lista: 
           self.listaCli.insert("", END, values=i) 
        self.desconectar_db() 
 
    def OnDoubleClik(self,event):#indicamos que o python vai realizar um um evento 
        self.limpa_cliente() 
        self.listaCli.selection() 
 
        for n in self.listaCli.selection(): 
            col1, col2, col3, col4 = self.listaCli.item(n, 'values') 
            self.codigo_entry.insert(END, col1)  # puxar os dados da coluna 1 
            self.nome_entry.insert(END, col2) 
            self.telefone_entry.insert(END, col3) 
            self.cidade_entry.insert(END, col4) 
 
    def deleta_cliente(self): 
        self.Variaveis() 
        self.conecta_db() 
        self.cursor.execute("""DELETE FROM clientes WHERE cod=?""",(self.codigo)) 
        self.conn.commit() 
        self.desconectar_db() 
        self.limpa_cliente() 
        self.select_lista() 
 
    def alterar_cliente(self): 
        self.Variaveis() 
        self.conecta_db() 
        self.cursor.execute("""UPDATE clientes SET nome_cliente=?,telefone=?,cidade=? WHERE 
cod=?""", 
            (self.nome,self.telefone,self.cidade,self.codigo)) 
        self.conn.commit() 
        self.desconectar_db() 
        self.select_lista() 
        self.limpa_cliente() 
 
#   Criando um for para extrair os dados 
 
class Application(funcs): 
    def __init__(self): 
        self.root = root 
        self.tela() 
        self.frames_da_tela() 
        self.criando_botoes() 
        self.lista_frame2() 
        self.montartabela() 
        self.select_lista() 
        root.mainloop() 
 
 
    def tela(self): 
        self.root.title("Cadastro de Clientes") 
        self.root.configure(background="blue") 
        self.root.geometry("700x500") 
        self.root.resizable(True, True) 
        self.root.maxsize(width=988, height=788) 
        self.root.minsize(width=500, height=400) 
 
    def frames_da_tela(self): 
        self.frame1 = Frame(self.root, bd=4, bg="#CCCCCC", 
                            highlightbackground="#759f06", highlightthickness=3) 
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46) 
 
        self.frame2 = Frame(self.root, bd=4, bg="#CCCCCC", 
                            highlightbackground="#759f06", highlightthickness=3) 
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46) 
 
    def criando_botoes(self): 
        # Criação do botão limpar 
        self.bt_limpar = Button(self.frame1, text="Limpar", bd=2, bg="#107db2", fg="white", 
font=("verdana", 8 
                                 , "bold"),command=self.limpa_cliente) 
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15) 
        # Criação do botão buscar 
        self.bt_buscar = Button(self.frame1, text="Buscar", bd=2, bg="#107db2", fg="white", 
                                font=("verdana", 8, "bold",)) 
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15) 
 
        # Criação do botão novo 
 
        self.bt_novo = Button(self.frame1, text="Novo", bd=2, bg="#107db2", fg="white", 
font=("verdana", 8, 
                                 "bold"), command=self.add_cliente) 
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15) 
 
        # Criação do botão alterar 
        self.bt_alterar = Button(self.frame1, text="Alterar", bd=2, bg="#107db2", fg="white", 
font=("verdana", 8, 
                                 "bold"), command=self.alterar_cliente) 
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15) 
 
        # Criação do botão apagar 
 
        self.bt_apagar = Button(self.frame1, text="Apagar", bd=2, bg="#107db2", fg="white", 
font=("verdana", 8, 
                                    "bold"),command=self.deleta_cliente) 
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15) 
 
        # criando label 
        self.lb_codigo = Label(self.frame1, text="Código", bg="#dfe3ee", fg="#107db2") 
        self.lb_codigo.place(relx=0.05, rely=0.05) 
 
        self.codigo_entry = Entry(self.frame1) 
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08) 
 
        # Criação de label e entrada de nome 
        self.lb_nome = Label(self.frame1, text="Nome", bg="#dfe3ee", fg="#107db2") 
        self.lb_nome.place(relx=0.05, rely=0.35) 
 
        self.nome_entry = Entry(self.frame1) 
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8) 
 
        # Criação da lebel entrada de telefone 
        self.lb_telefone = Label(self.frame1, text="Telefone", bg="#dfe3ee", fg="#107db2") 
        self.lb_telefone.place(relx=0.05, rely=0.6) 
 
        self.telefone_entry = Entry(self.frame1) 
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4) 
 
        # Criação da lebel entrada de Cidade 
        self.lb_cidade = Label(self.frame1, text="Cidade", bg="#dfe3ee", fg="#107db2") 
        self.lb_cidade.place(relx=0.5, rely=0.6) 
 
        self.cidade_entry = Entry(self.frame1) 
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4) 
 
    # lista frame2 
    def lista_frame2(self): 
        self.listaCli= ttk.Treeview(self.frame2, height=3, columns=("coll", "coll2", "coll3", "coll4")) 
        self.listaCli.heading("#0", text="") 
        self.listaCli.heading("#1", text="Código") 
        self.listaCli.heading("#2", text="Nome") 
        self.listaCli.heading("#3", text="Telefone") 
        self.listaCli.heading("#4", text="Cidade") 
 
        self.listaCli.column("#0", width=1) 
        self.listaCli.column("#1", width=50) 
        self.listaCli.column("#2", width=200) 
        self.listaCli.column("#3", width=125) 
        self.listaCli.column("#4", width=125) 
 
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85) 
        # criando barra de rolagem 
        self.scroollista = Scrollbar(self.frame2, orient="vertical") 
        self.listaCli.configure(yscroll=self.scroollista.set) 
        self.scroollista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85) 
        #criando a função para chamar o Onclic 
        self.listaCli.bind("<Double-1>",self.OnDoubleClik)#usamos bind toda vez que precisamos 
        #Double serve para toda vez que damos os dois click 
 
 
Application() 