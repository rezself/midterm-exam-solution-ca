def listaGrafo(aristas, nodos):
    grafo = [[] for i in range(nodos)]
    for (de, a) in aristas:
        grafo[de-1].append(a)
    return grafo

# def clasificarPrimeros(grafo, nodos):
#    primeros = []
#    for i in range(nodos):
#        esPrimero = True
#        for n in range(len(grafo[i])):
#            if grafo[i][n] == (i+1):
#                esPrimero = False
#        if esPrimero:
#            primeros.append(i+1) 

if __name__ == '__main__':
    aristas = [(2, 1), (2, 10), (3, 8), (3, 9), (3, 10), (6, 5), (6, 7), (7, 4), (8, 2), (8, 4), (8, 5)]
    nodos = 10
    grafo = listaGrafo(aristas, nodos)
    #clasificarPrimeros(grafo, nodos)