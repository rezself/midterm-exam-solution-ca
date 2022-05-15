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

def encontrarNodoRaiz(grafo, n):
    completo = []
    for m in range(n):
        completo.append(m)

    for i in range(n):
        visitado = []
        DFS(visitado, grafo, i)
        visitado.sort()

        if completo == visitado:
            return i
    return -1

#main
if __name__ == '__main__':
    # Lista de aristas según el grafo
    aristas = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 3), (4, 5), (5, 0)]
    # Total de nodos en el grafo
    n = 6
    #Convertir a lista de adyacencia
    grafo = listaGrafo(aristas, n)
    #Es fuertemente conectado o no
    raiz = encontrarNodoRaiz(grafo, n)
    if raiz != -1:
        print(raiz)
    else:
        print(-1)