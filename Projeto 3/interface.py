<<<<<<< HEAD
from tkinter import *
from tkinter import filedialog
import logging
import threading
from transmit import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Transmissor GUI")
        self.msg.pack ()
        self.filename = " "

        self.fonteGrande = ("Arial","16")
        self.fontePadrao = ("Helvetica", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 30
        self.quintoContainer["padx"] = 15
        self.quintoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Nome do arquivo jpeg a ser enviado \n (deve estar na pasta deste script!)")
        self.titulo["font"] = ("Helvetica", "10")
        self.titulo.pack()
  
  
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 32
        self.nome["text"] = self.filename
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.selecionar = Button(self.segundoContainer)
        self.selecionar["text"] = "Selecionar"
        self.selecionar["font"] = ("Calibri", "8")
        self.selecionar["width"] = 14
        self.selecionar["command"] = self.selecionaArquivo
        self.selecionar.pack(side=RIGHT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Enviar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["command"] = self.transmitir
        self.autenticar.pack()



    def selecionaArquivo(self):
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        self.filename = root.filename
        self.nome.insert(0,self.filename)
        # if len(self.filename) > 0:
        #     self.log.delete(0, 'end')
        #     self.log["fg"] = "green"
        #     self.log.insert(0,"Arquivo selecionado")
        # else:
        #     self.log.delete(0, 'end')
        #     self.log["fg"]="yellow"
        #     self.log.insert(0,"Arquivo não selecionado")
        print("aa")
    def transmitir(self):
        if len(self.filename) > 1:
            print("entrou")
            main(self.filename)
            # self.log["fg"] = "green"
            # self.log.insert(0,"Envio Concluído!")
        else:
            print(len(self.filename))
            print(self.filename)
        
root = Tk()
Application(root)
=======
from tkinter import *
from tkinter import filedialog
import logging
import threading
from transmit import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Transmissor GUI")
        self.msg.pack ()
        self.filename = " "

        self.fonteGrande = ("Arial","16")
        self.fontePadrao = ("Helvetica", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 30
        self.quintoContainer["padx"] = 15
        self.quintoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Nome do arquivo jpeg a ser enviado \n (deve estar na pasta deste script!)")
        self.titulo["font"] = ("Helvetica", "10")
        self.titulo.pack()
  
  
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 32
        self.nome["text"] = self.filename
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.selecionar = Button(self.segundoContainer)
        self.selecionar["text"] = "Selecionar"
        self.selecionar["font"] = ("Calibri", "8")
        self.selecionar["width"] = 14
        self.selecionar["command"] = self.selecionaArquivo
        self.selecionar.pack(side=RIGHT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Enviar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["command"] = self.transmitir
        self.autenticar.pack()



    def selecionaArquivo(self):
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        self.filename = root.filename
        self.nome.insert(0,self.filename)
        # if len(self.filename) > 0:
        #     self.log.delete(0, 'end')
        #     self.log["fg"] = "green"
        #     self.log.insert(0,"Arquivo selecionado")
        # else:
        #     self.log.delete(0, 'end')
        #     self.log["fg"]="yellow"
        #     self.log.insert(0,"Arquivo não selecionado")
        print("aa")
    def transmitir(self):
        if len(self.filename) > 1:
            print("entrou")
            main(self.filename)
            # self.log["fg"] = "green"
            # self.log.insert(0,"Envio Concluído!")
        else:
            print(len(self.filename))
            print(self.filename)
        
root = Tk()
Application(root)
>>>>>>> 1b901fa4757ed8d0341dd3432800f89bafae2549
root.mainloop()