from tkinter import *
import math

class Interface ():
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.segundoContainer2 = Frame(master)
        self.segundoContainer2["padx"] = 20
        self.segundoContainer2.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 1
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 1
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Calculadora de Bhaskara", font=self.fontePadrao)
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.numA = Label(self.segundoContainer,text="A", font=self.fontePadrao)
        self.numA.pack(side=LEFT)

        self.numA = Entry(self.segundoContainer)
        self.numA["width"] = 30
        self.numA["font"] = self.fontePadrao
        self.numA.pack(side=LEFT)

        self.numB = Label(self.segundoContainer2, text="B", font=self.fontePadrao)
        self.numB.pack(side=LEFT)

        self.numB = Entry(self.segundoContainer2)
        self.numB["width"] = 30
        self.numB["font"] = self.fontePadrao
        self.numB.pack(side=LEFT)

        self.numC = Label(self.terceiroContainer, text="B", font=self.fontePadrao)
        self.numC.pack(side=LEFT)

        self.numC = Entry(self.terceiroContainer)
        self.numC["width"] = 30
        self.numC["font"] = self.fontePadrao
        self.numC.pack(side=LEFT)


        self.calcular = Button(self.quartoContainer)
        self.calcular["text"] = "Calcular"
        self.calcular["font"] = ("Calibri", "8")
        self.calcular["width"] = 12
        self.calcular["command"] = self.pegarDados
        self.calcular.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.mensagem2 = Label(self.quintoContainer, text="", font=self.fontePadrao)
        self.mensagem2.pack()

    def pegarDados(self):
        self.a = self.numA.get()
        self.b = self.numB.get()
        self.c = self.numC.get()
        self.a = int(self.a)
        self.b = int(self.b)
        self.c = int(self.c)
        self.raiz = self.b*self.b-4*self.a*self.c
        self.raiz = math.sqrt(self.raiz)
        self.baixo = 2*self.a
        self.deltaPos = (-self.b+self.raiz)/self.baixo
        self.deltaNeg = (-self.b-self.raiz)/self.baixo
        self.mensagem["text"] = "Valor A:",self.deltaPos
        self.mensagem2["text"] = "Valor B:",self.deltaNeg

root = Tk()
root.title("Calculadora de Bhaskara")
Interface(root)
root.mainloop()