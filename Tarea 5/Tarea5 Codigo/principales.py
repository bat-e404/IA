from colorama import Fore,Back
def imprimir_tablero(tablero):
    texto = ""
    for i in range(1,10):
        if tablero[i-1] == '.':
            texto += f'\t{i}'
        else:
            texto += '\t' + Fore.RED + tablero[i-1] + Fore.RESET
        if i%3 == 0:
            texto += '\n'
    print(texto)

def evaluar_tablero(tablero):
    #return -1 cuando ganas
    #return 1 cuando pierdes
    #return 0 cuando es empate
    #return -2 NO es nodo terminal
    c_central = tablero[4]
    
    if c_central != ".":
        #Verificamos si en las digonales se ha ganado
        if tablero[0] == c_central and tablero[8] == c_central or tablero[6] == c_central and tablero[2] == c_central :
            if c_central == 'X':
                return -1
            else:
                return 1
        
        #Verificamos si en la fila y columna que contenga c_central se ha ganado
        if tablero[1] == c_central and tablero[7] == c_central or tablero[3] == c_central and tablero[5] == c_central:
            if c_central == 'X':
                return -1
            else:
                return 1

    #Verificamos si en las filas y columnas restantes se ha ganado
    c_esquina1 = tablero[0] 
    if c_esquina1 != '.':  
        if tablero[1] == c_esquina1 and tablero[2] == c_esquina1 or tablero[3] == c_esquina1 and tablero[6] == c_esquina1:
            if c_esquina1 == 'X':
                return -1
            else:
                return 1
    
    c_esquina2 = tablero[8] 
    if c_esquina2 != '.':
        if tablero[2] == c_esquina2 and tablero[5] == c_esquina2 or tablero[6] == c_esquina2 and tablero[7] == c_esquina2:
            if c_esquina2 == 'X':
                return -1
            else:
                return 1

    #Verificamos si NO es un nodo terminal
    for i in range(0,9):
        if tablero[i] == '.':
            return -2
    
    #Si no se cumple ningun caso anterior entonces es  Empate
    return 0
