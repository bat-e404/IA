from tkinter import *
from frames import *
from tkinter import messagebox

ventana = Tk()                                  # VENTANA  RAIZ
ventana.geometry("700x600")                     # DIMENCIONES DE LA VENTANA RAIZ
ventana.title("Tres en raya")                   # TITULO DE LA VENTANA RAIZ
ventana.resizable(0,0)

cargar_ventana(ventana)

ventana.mainloop()