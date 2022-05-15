#Se crea lista de adyacencia
def listaGrafo(aristas, n):
    grafo = [[] for i in range(n)]
    for (de, a) in aristas:
        grafo[de].append(a)
    return grafo

#DFS
def DFS(visitado, grafo, nodo):
    if nodo not in visitado:
        visitado.append(nodo)

        for nodo in grafo[nodo]:
            DFS(visitado, grafo, nodo)

def esFuertementeConectado(grafo, n):
    for i in range(n):
        visitado = []
        DFS(visitado, grafo, i)
        
        for n in range(n):
            var = False
            for m in visitado:
               if visitado[m] == n:
                   var = True
            if var == False:
                return False
    return True

#main
if __name__ == '__main__':
    # Lista de aristas según el grafo
    aristas = [(0, 4), (1, 0), (1, 2), (2, 1), (2, 4), (3, 1), (3, 2), (4, 3)]
    # Total de nodos en el grafo
    n = 5
    #Convertir a lista de adyacencia
    grafo = listaGrafo(aristas, n)
    #Es fuertemente conectado o no
    if esFuertementeConectado(grafo, n):
        print('1 (si es fuertemente conectado SCC)')
    else:
        print('0 (no es fuertemente conectado)')
