from tkinter import *
from tkinter import messagebox
from principales import evaluar_tablero,imprimir_tablero
from nodo import Nodo

class Marcador():

    def __init__(self):
        self.victorias=0
        self.derrotas=0
        self.empates=0

    def getVic(self):
        return self.victorias
    def getDer(self):
        return self.derrotas
    def getEmp(self):
        return self.empates
    
    def incVic(self):
        self.victorias += 1
    def incDer(self):
        self.derrotas += 1
    def incEmp(self):
        self.empates += 1
def incVic(texto):
    marc.incVic()
    texto.config(text=f"Victorias: {marc.getVic()}")
def incDer(texto):
    marc.incDer()
    texto.config(text=f"Derrotas: {marc.getDer()}")
def incEmp(texto):
    marc.incEmp()
    texto.config(text=f"Empates: {marc.getEmp()}")
marc=Marcador()
v=0
e=0
d=0
lista=[]
def cargar_ventana(ventana):
    # CREAMOS EL CONTENEDOR
    encabezado = Frame(ventana, width=700, height=120)

    # AGREGAMOS ESTILOS AL CONTENEDOR
    encabezado.config(bg="Black")

    # OBJETOS DEL CONTENEDOR
    titulo = Label(encabezado,width=12)
    titulo.config(
        text="Tres en raya",
        bg="Black",
        fg="Yellow",
        font=('Stencil',40)
    )
    titulo.pack()

    # EMPAQUETAMOS CONTENEDOR
    encabezado.pack(fill=X, expand=True, side=TOP, anchor=N)
    encabezado.pack_propagate(False)    


    #FUENTE Y TAMAÑO DE LA LETRA
    fuente = ('Fixedsys',18)
    fondo = "Black"
    color = "lime"


    # CREAMOS EL CONTENEDOR
    marcador = Frame(encabezado, width=700, height=50)

    # AGREMOS ESTILO AL CONTENEDOR
    marcador.config(bg=fondo)

    # OBJETOS DEL CONTENEDOR
    victorias = Label(marcador)
    empates = Label(marcador)
    derrotas = Label(marcador)

    # AGREGAMOS ESTILOS A LOS OBJETOS
    victorias.config(
        text=f"Victoria: {marc.getVic()}",
        width=10,
        bg=fondo,
        fg=color,
        font=fuente
    )
    empates.config(
        text=f"Empates: {marc.getEmp()}",
        width=10,
        bg=fondo,
        fg=color,
        font=fuente
    )
    derrotas.config(
        text=f"Derrotas: {marc.getDer()}",
        width=10,
        bg=fondo,
        fg=color,
        font=fuente
    )

    # EMPAQUTAMOS LOS OBJETOS AL CONTENEDOR
    victorias.pack(side=LEFT, fill=X, expand=True)
    empates.pack(side=LEFT, fill=X, expand=True)
    derrotas.pack(side=LEFT, fill=X, expand=True)

    # EMPAQUETAMOS EL CONTENEDOR
    marcador.pack(fill=X, expand=True, side=TOP, anchor=N)
    marcador.pack_propagate(False)


    # FONDO DEL CONTENEDOR(menu)
    fondo="lightBlue"
    # FUENTE
    fuente =  "Fixedsys"

    # CREAMOS EL CONTENEDOR
    menu = Frame(ventana)

    # AGREGAMOS ESTILO AL CONTENEDOR
    menu.config(
        width=200,
        height=480,
        bg=fondo
    )

    # OBJETOS DEL CONTENEDOR
    titulo = Label(menu)
    empezar = Button(menu)    
    reiniciar = Button(menu)
    pregunta = Label(menu)
    respuesta1 = Radiobutton(menu)
    respuesta2 = Radiobutton(menu)        
    void = Label(menu)
    void1 = Label(menu)
    void2 = Label(menu)
    opcion = StringVar()
    opcion.set(None)

    def f_reiniciar(tablero):
        for casilla in tablero:
            casilla.config(
                text=" ",
                fg="Black"                
            )

    # AGREGAR ESTILOS A LOS OBJETOS
    titulo.config(
        text="Menu Principal",
        bg=fondo,
        font=('fuente',17)
    )
    empezar.config(
        text="Empezar",
        font=(fuente,16),
        padx=10,
        pady=10,        
    )    
    reiniciar.config(
        text="Reiniciar",
        font=(fuente,16),
        command=lambda:f_reiniciar(lista),
        padx=10,
        pady=10      
    )
    pregunta.config(
        text="¿Quien iniciara\nla partida?",
        font=(fuente,16),
        padx=10,
        bg=fondo
    )
    respuesta1.config(
        text="Player",
        value="Player",
        variable=opcion,
        font=(fuente,16),
        bg=fondo        
    )
    respuesta2.config(
        text="Maquina",
        value="Maquina",
        variable=opcion,
        font=(fuente,16),
        bg=fondo        
    )
    void.config(
        text=" ",
        font=('Mistral',1),
        height=1,
        bg=fondo
        )
    void1.config(
        text=" ",
        font=('Mistral',1),
        height=1,
        bg=fondo
        )
    void2.config(
        text=" ",
        font=('Mistral',12),
        height=1,
        bg=fondo
        )        

    # EMPAQUETAMOS LOS OBJETOS
    titulo.pack()
    void.pack()
    empezar.pack()
    void1.pack()
    reiniciar.pack()
    void2.pack()
    pregunta.pack()
    respuesta1.pack()
    respuesta2.pack()

    # EMPAQUETAMOS EL CONTENEDOR
    menu.place(x=0,y=120)
    menu.pack_propagate(False)


    #FUENTE Y TAMAÑO DE LA LETRA(tablero)
    fuente=('Fixedsys',50)

    # FONDO DEL CONTENEDOR(tablero)
    fondo="#31FA31"

    # CREAMOS EL CONTENEDOR
    tablero = Frame(ventana)

    # AGREGAMOS LOS ESTILOS AL CONTENEDOR
    tablero.configure(
        width=500,
        height=480,
        bd=15,
        bg=fondo
    )

    # OBJETOS DEL CONTENEDOR
    fila1 = Frame(tablero)
    fila2 = Frame(tablero)
    fila3 = Frame(tablero)
    casilla1 = Button(fila1)
    casilla2 = Button(fila1)
    casilla3 = Button(fila1)
    casilla4 = Button(fila2)
    casilla5 = Button(fila2)
    casilla6 = Button(fila2)
    casilla7 = Button(fila3)
    casilla8 = Button(fila3)
    casilla9 = Button(fila3)
    void = Label(tablero)

    # AGREGAMOS LOS ESTILOS A LOS OBJETOS
    casilla1.config(
        text=" ",
        width=3,
        height=1,
        padx=10,
        pady=10,
        font=fuente,
        relief=SOLID,
        bg=fondo,
        fg="Black",
        command=lambda: colocar_ficha(casilla1,opcion,victorias,derrotas,empates)
    )
    casilla2.config(
        text=" ",
        width=3,
        height=1,
        padx=10,
        pady=10,
        font=fuente,
        relief=SOLID,
        bg=fondo,
        fg="Black",
        command=lambda: colocar_ficha(casilla2,opcion,victorias,derrotas,empates)
    )
    casilla3.config(
        text=" ",
        width=3,
        height=1,
        padx=10,
        pady=10,
        font=fuente,
        relief=SOLID,
        bg=fondo,
        fg="Black",
        command=lambda: colocar_ficha(casilla3,opcion,victorias,derrotas,empates)
    )
    casilla4.config(
        text=" ",
        width=3,
        height=1,
        padx=10,
        pady=10,
        font=fuente,
        relief=SOLID,
        bg=fondo,
        fg="Black",
        command=lambda: colocar_ficha(casilla4,opcion,victorias,derrotas,empates)
    )
    casilla5.config(
        text=" ",
        width=3,
        height=1,
        padx=10,
        pady=10,
        font=fuente,
        relief=SOLID,
        bg=fondo,
        fg="Black",
        command=lambda: colocar_ficha(casilla5,opcion,victorias,derrotas,empates)
    )
    casilla6.config(
        text=" ",
        width=3,
        height=1,
        padx=10,
        pady=10,
        font=fuente,
        relief=SOLID,
        bg=fondo,
        fg="Black",
        command=lambda: colocar_ficha(casilla6,opcion,victorias,derrotas,empates)
    )
    casilla7.config(
        text=" ",
        width=3,
        height=1,
        padx=10,
        pady=10,
        font=fuente,
        relief=SOLID,
        bg=fondo,
        fg="Black",
        command=lambda: colocar_ficha(casilla7,opcion,victorias,derrotas,empates)
    )
    casilla8.config(
        text=" ",
        width=3,
        height=1,
        padx=10,
        pady=10,
        font=fuente,
        relief=SOLID,
        bg=fondo,
        fg="Black",
        command=lambda: colocar_ficha(casilla8,opcion,victorias,derrotas,empates)
    )
    casilla9.config(
        text=" ",
        width=3,
        height=1,
        padx=10,
        pady=10,
        font=fuente,
        relief=SOLID,
        bg=fondo,
        fg="Black",
        command=lambda: colocar_ficha(casilla9,opcion,victorias,derrotas,empates)
    )
    void.config(
        text=" ",
        font=('Mistral',12),
        width=1,
        height=60,
        bg=fondo
        )  
    
    # EMPAQUETAMOS LOS OBJETOS
    void.pack(side=LEFT,anchor=N)
    fila1.pack()
    fila2.pack()
    fila3.pack()
    casilla1.pack(side=LEFT, anchor=N)
    casilla2.pack(side=LEFT, anchor=N)
    casilla3.pack(side=LEFT, anchor=N)
    casilla4.pack(side=LEFT, anchor=N)
    casilla5.pack(side=LEFT, anchor=N)
    casilla6.pack(side=LEFT, anchor=N)
    casilla7.pack(side=LEFT, anchor=N)
    casilla8.pack(side=LEFT, anchor=N)
    casilla9.pack(side=LEFT, anchor=N)    

    
    #LISTA(tablero)
    lista.append(casilla1)
    lista.append(casilla2)
    lista.append(casilla3)
    lista.append(casilla4)
    lista.append(casilla5)
    lista.append(casilla6)
    lista.append(casilla7)
    lista.append(casilla8)
    lista.append(casilla9)

    # EMPAQUETAMOS EL CONTENEDOR
    tablero.place(x=200,y=120)
    tablero.pack_propagate(False)

def leer_tablero(lista):
    tablero=[]
    for cas in lista:
        c=cas['text']
        c=c.upper()
        if c != ' ':
            tablero.append(c)
        else:
            tablero.append('.')
    return tablero
def colocar_ficha(casilla,opcion,victorias,derrotas,empates):
    if opcion.get() != 'None':
        tablero = leer_tablero(lista)
        vacio=True
        for cas in tablero:
            if cas != '.':
                vacio = False
                break                    

        #COLOCAMOS FICHA
        if vacio and opcion.get()=='Maquina':            
            if evaluar_tablero(tablero) == -2:
                nodo_inicial = Nodo(tablero,"O")
                Nodo_optimo = nodo_inicial.nodo_optimo
                tablero_nodo_optimo = Nodo_optimo.getTablero()
                casilla_optima = 0
                for casilla_i in tablero:
                    if tablero[casilla_optima] != tablero_nodo_optimo[casilla_optima]:
                        break
                    casilla_optima += 1                
                casilla = lista[casilla_optima]
                casilla.config(
                    text="o",
                    fg="Blue"
                )
                tablero = leer_tablero(lista)
                imprimir_tablero(tablero)
        else:
            if evaluar_tablero(tablero)==-2 and casilla['text']==' ':
                casilla.config(
                    text="x",
                    fg="red"
                )
                tablero=leer_tablero(lista)
                resultado=evaluar_tablero(tablero)
                
                #Creamos el arbol y buscamos la mejor jugada para la IA
                if resultado == -2:
                    nodo_inicial = Nodo(tablero,"O")
                    Nodo_optimo = nodo_inicial.nodo_optimo
                    tablero_nodo_optimo = Nodo_optimo.getTablero()
                    casilla_optima = 0
                    for casilla_i in tablero:
                        if tablero[casilla_optima] != tablero_nodo_optimo[casilla_optima]:
                            break
                        casilla_optima += 1
                    imprimir_tablero(tablero)
                    casilla = lista[casilla_optima]
                    casilla.config(
                        text="o",
                        fg="Blue"
                    )        
    else:        
        messagebox.showinfo("Partida","Selecciona quien iniciara la partida!")
    
    tablero_l = leer_tablero(lista)
    resultado=evaluar_tablero(tablero_l)
    if resultado==-1: #ganar
        messagebox.showinfo("Resultado de la partida","Felicidades has ganado!")
        incVic(victorias)
    elif resultado==1: #perdiste
        messagebox.showinfo("Resultado de la partida","Suerte para la proxima!\nPerdiste :(")
        incDer(derrotas)
    elif resultado==0: #empate
        messagebox.showinfo("Resultado de la partida","Nadie gano\nsera la proxima ves!")
        incEmp(empates)
