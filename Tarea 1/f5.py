from sympy import expand

def expresion(e):
    return expand(e)

userExpresion = "(2 * (x + 1) * (y + 3))"

print("La expresion: ",userExpresion,"Simplificada es: ", expresion(userExpresion))
