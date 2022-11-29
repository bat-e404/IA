arbol = [[[1,2],3],[4,[5,6]],[7],[8,9,10]]

def arbol_ref(arbol, tupla):

    listaArbol = list(tupla)
    n = len(listaArbol)
    
    if(n == 1):
        print(arbol[listaArbol[0]])
    if(n == 2):
        print(arbol[listaArbol[0]][listaArbol[1]])
    if(n == 3):
        print(arbol[listaArbol[0]][listaArbol[1]][listaArbol[2]])
    
arbol_ref(arbol,(1,))

    
    

