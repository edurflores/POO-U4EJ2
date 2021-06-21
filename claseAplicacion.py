import tkinter as tk
from tkinter import ttk

from apidolar import Dolar

class Aplicacion(tk.Tk):
    __dolaractual=Dolar
    def __init__(self):
        self.__dolaractual = Dolar()
        super().__init__()
        self.title("Conversor de dolar")
        self.geometry("300x150")
        self.config(padx=2,pady=2)
        self.resizable(0,0)
        self.__dolares= tk.DoubleVar()
        self.__dolares.trace("w", self.calculo)
        self.__pesos=tk.DoubleVar()

        self.__frame = ttk.Frame(self, padding="3 3 10 10")
        self.__frame["relief"] = "sunken"
        self.__edolar = ttk.Entry(self.__frame, width=8, textvariable=self.__dolares)
        self.__lbdolar= ttk.Label(self.__frame, text="dólares")
        self.__lbequiv= ttk.Label(self.__frame, text="es equivalente a \t\t pesos")
        self.__lbpesos=ttk.Label(self.__frame, textvariable=self.__pesos)
        self.__exit=ttk.Button(self.__frame, text="SALIR", command=self.destroy)

        self.__frame.place(anchor=tk.CENTER, relwidth=1, relheight=1, relx=0.5, rely=0.5)
        self.__edolar.place(anchor= tk.CENTER, relwidth = 0.2, relheight=0.2, relx=0.3, rely=0.2)
        self.__lbdolar.place(anchor=tk.CENTER, relwidth = 0.3, relheight=0.2, relx=0.6, rely=0.2)
        self.__lbequiv.place(anchor=tk.CENTER, relwidth = 0.7, relheight=0.2, relx=0.4, rely=0.5)
        self.__lbpesos.place(anchor=tk.CENTER, relwidth = 0.2,  relheight=0.2, relx=0.48, rely=0.5)
        self.__exit.place(anchor=tk.E, relwidth = 0.3, relheight= 0.2, relx=1, rely = 0.7)

    def calculo(self, *args):
        self.__pesos.set(float(self.__edolar.get())*self.__dolaractual.obtener())