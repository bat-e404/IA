from collections import deque
import time
inicio = time.time() 
# Una clase para representar un objeto grafo
class Graph:
    # Constructor
    def __init__(self, edges, n):
 
        # Una lista de listas para representar una lista de adyacencia
        self.adjList = [[] for _ in range(n)]
 
        # agrega bordes al grafo no dirigido
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
# Realizar BFS en el graph a partir del vértice `v`
def BFS(graph, v, discovered):
 
    # crea una queue para hacer BFS
    q = deque()
 
    # marca el vértice de origen como descubierto
    discovered[v] = True
 
    # poner en queue el vértice fuente
    q.append(v)
 
    # Bucle # hasta que la queue esté vacía
    while q:
 
        # quitar la queue del nodo frontal e imprimirlo
        v = q.popleft()
        print(v, end=' ')
 
        # do para cada arista (v, u)
        for u in graph.adjList[v]:
            if not discovered[u]:
                # marcarlo como descubierto y ponerlo en queue
                discovered[u] = True
                q.append(u)
 
 
if __name__ == '__main__':
 
    # Lista de bordes de graph según el diagrama anterior
    edges = [
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11),(11,12),(11,13),(13,14),(13,15),(15,13),(13,16),(16,17)
        # vértice 0, 13 y 14 son nodos individuales
    ]
 
    # número total de nodos en el graph (etiquetados de 0 a 19)
    n = 19
 
    # construye un graph a partir de los bordes dados
    graph = Graph(edges, n)
 
    # para realizar un seguimiento de si se descubre un vértice o no
    discovered = [False] * n
 
    # Realizar el recorrido BFS de todos los nodos no descubiertos a
    # cubre todos los componentes conectados de un graph
    for i in range(n):
        if not discovered[i]:
            # inicia el recorrido BFS desde el vértice i
            BFS(graph, i, discovered)

fin = time.time()
print(" ") 
print("Tiempo de ejecucion: ") 
print(fin-inicio)