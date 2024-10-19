from tkinter import *
from tkinter import ttk
import tkinter as tk

class Application:
    def __init__(self):
        self.root = Tk()  
        self.tela() 
        self.frames_da_tela()   
        self.lista_frame2()
        self.barra_rolagem()
        self.criando_botoes() 
        self.criando_label()  
        self.root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(bg='#1e3743')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=400, height=300)
    
    def frames_da_tela(self):
        self.frame_1=Frame(
        self.root, bd=4, bg="#dfe3ee",
        highlightbackground="#FFD700", highlightthickness=3,
        
        )
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)   
        self.frame_2=Frame(
        self.root, bd=4, bg="#dfe3ee",
        highlightbackground="#FFD700", highlightthickness=3,
        
        )
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)   
        
    def criando_botoes(self):
        #Criação do botão limpar
        self.bt_limpar=Button(self.frame_1,text="Limpar")
        self.bt_limpar.place(relx=0.2, rely=0.1,relheight=0.15, relwidth=0.1)
        #Criação do botão buscar
        self.bt_limpar=Button(self.frame_1, text="Buscar")
        self.bt_limpar.place(relx=0.3, rely=0.1,relheight=0.15, relwidth=0.1 )
        # Criação do botão novo
        self.bt_limpar = Button(self.frame_1, text="Novo")
        self.bt_limpar.place(relx=0.6, rely=0.1, relheight=0.15, relwidth=0.1)
        # Criação do botão alterar
        self.bt_limpar = Button(self.frame_1, text="Altera")
        self.bt_limpar.place(relx=0.7, rely=0.1, relheight=0.15, relwidth=0.1)
        # Criação do botão apagar
        self.bt_limpar = Button(self.frame_1, text="Apagar")
        self.bt_limpar.place(relx=0.8, rely=0.1, relheight=0.15, relwidth=0.1)
        #Criação Label
        self.lb_codigo=Label(self.frame_1, text="Código")
        self.lb_codigo.place(relx=0.05, rely=0.05)


    def criando_label(self):
        self.codigo_entry=Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05,rely=0.15,relwidth=0.08)

        # Criação de label e entrada de nome
        self.lb_nome = Label(self.frame_1, text="Nome")
        self.lb_nome.place(relx=0.06, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)
        
        # Criação da lebel entrada de telefone
        self.lb_nome = Label(self.frame_1, text="Telefone", bg="#dfe3ee", fg="#107db2")
        self.lb_nome.place(relx=0.05, rely=0.6)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.7)
        
         # Criação da lebel entrada de cidade
        self.lb_nome = Label(self.frame_1, text="Cidade", bg="#dfe3ee", fg="#107db2")
        self.lb_nome.place(relx=0.30, rely=0.6)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.30, rely=0.7)
        
    def lista_frame2(self):
        self.listaCli=ttk.Treeview(self.frame_2,height=3, columns=("coll","coll2","coll3","col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")
        
        self.listaCli.column(column="#0", width=1)
        self.listaCli.column(column="#1", width=50)
        self.listaCli.column(column="#2", width=208)
        self.listaCli.column(column="#3", width=125)
        self.listaCli.column(column="#4", width=125)
        
        self.listaCli.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.85)
        
    def barra_rolagem(self):
        # Criando a barra de rolagem vertical
        self.Scroollist = Scrollbar(self.frame_2, orient="vertical")

        # Configurando a lista para usar a barra de rolagem
        self.listaCli.config(yscrollcommand=self.Scroollist.set)

        # Posicionando a barra de rolagem
        self.Scroollist.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

        # Conectando a barra de rolagem à lista
        self.Scroollist.config(command=self.listaCli.yview)
        
Application()
