import re

def cuenta_patron(buscar,texto):
    listTexto = re.findall(r"(?=("+buscar+"))",texto)
    return len(listTexto)

buscar = input("Texto a buscar: ")
texto = input("Texto: ")

print("Numero de repeticiones:",cuenta_patron("aba","gabababa"))