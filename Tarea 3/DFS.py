from collections import deque
import time
inicio = time.time()

# Una clase para representar un objeto graph
class Graph:
    # Constructor
    def __init__(self, edges, n):
 
        # Una lista de listas para representar una lista de adyacencia
        self.adjList = [[] for _ in range(n)]
 
        # agrega bordes al graph no dirigido
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
# Realizar DFS iterativo en el graph a partir del vértice `v`
def iterativeDFS(graph, v, discovered):
 
    # crea una stack utilizada para hacer DFS iterativo
    stack = deque()
 
    # inserta el nodo de origen en la stack
    stack.append(v)
 
    # Bucle # hasta que la stack esté vacía
    while stack:
 
        # Extrae un vértice de la stack
        v = stack.pop()
 
        # si el vértice ya está descubierto, ignóralo
        if discovered[v]:
            continue
 
        # llegaremos aquí si el vértice reventado `v` aún no se descubre;
        # imprime `v` y procesa sus nodos adyacentes no descubiertos en la stack
        discovered[v] = True
        print(v, end=' ')
 
        # do para cada arista (v, u)
        adjList = graph.adjList[v]
        for i in reversed(range(len(adjList))):
            u = adjList[i]
            if not discovered[u]:
                stack.append(u)

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
        # Observe que el nodo 0 está desconectado
        (1,2),(2,3),(2,4),(4,3),(4,5),(5,2)
    ]
 
    # número total de nodos en el graph (etiquetados de 0 a 12)
    n = 7
 
    # construye un graph a partir de los bordes dados
    graph = Graph(edges, n)
 
    # para realizar un seguimiento de si se descubre un vértice o no
    discovered = [False] * n
 
    # Hacer un recorrido DFS iterativo desde todos los nodos no descubiertos hasta
    # cubre todos los componentes conectados de un graph
    for i in range(n):
        if not discovered[i]:
            iterativeDFS(graph, i, discovered)

    for i in range(n):
        if not discovered[i]:
            # inicia el recorrido BFS desde el vértice i
            BFS(graph, i, discovered)

fin = time.time()

print(" ") 
print("Tiempo de ejecucion: ") 
print(fin-inicio) 