from random import randint
from principales import evaluar_tablero
class Nodo():
    def __init__(self, tablero,turno):
        self.tablero = tablero
        self.turno = turno
        self.casillas_libres = []
        self.lista_relaciones = []
        self.estado = evaluar_tablero(self.tablero)
        self.valor = ""
        if turno == 'O':
            self.maximo = True
        else:
            self.maximo = False
        
        indice = 0
        for casilla in tablero:
            if casilla == '.':
                self.casillas_libres.append(indice)        
            indice += 1

        if self.estado == -2:            
            for indice in self.casillas_libres:
                tablero_aux = []
                for casilla in tablero:
                    tablero_aux.append(casilla)
                tablero_aux.insert(indice,turno)
                tablero_aux.pop(indice+1)
                if turno == "X":
                    turno_aux = 'O'
                else:
                    turno_aux = 'X'            
                self.lista_relaciones.append(Nodo(tablero_aux,turno_aux))
        if len(self.lista_relaciones) != 0:
            if self.maximo:
                self.nodo_optimo = self.max()
                self.valor = self.nodo_optimo.getValor()
            else:
                self.nodo_optimo = self.min()
                self.valor = self.nodo_optimo.getValor()
        else:
            self.valor = self.getEstado()
        


    #Metodos Get
    def getTablero(self):
        return self.tablero
    def getListaRelaciones(self):
        return self.lista_relaciones
    def getTurno(self):
        return self.turno
    def getCasillasLibres(self):
        return self.casillas_libres
    def getEstado(self):
        return self.estado
    def getValor(self):
        return self.valor
    def getNodoOptimo(self):
        return self.nodo_optimo
    

    #Metodos Set    
    def setTablero(self,tablero):
        self.tablero = tablero
    def setListaRelaciones(self,lista):
        self.lista_relaciones = lista
    def setTurno(self,turno):
        self.turno = turno
    
    #Metodos
    def max(self):
        long = len(self.lista_relaciones)-1
        maximo = self.lista_relaciones[randint(0,long)]
        for nodo_hijo in self.lista_relaciones:
            if nodo_hijo.valor > maximo.valor:
                maximo = nodo_hijo
        return maximo
    def min(self):
        long = len(self.lista_relaciones)-1
        minimo = self.lista_relaciones[randint(0,long)]
        for nodo_hijo in self.lista_relaciones:
            if nodo_hijo.valor < minimo.valor:
                minimo = nodo_hijo
        return minimo