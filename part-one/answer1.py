import random

listaGrafo = {
    '0' : ['1', '5'],
    '1' : ['0', '2', '3'],
    '2' : ['1', '3', '4'],
    '3' : ['1', '2', '5'],
    '4' : ['2', '5'],
    '5' : ['0', '3', '4']
}

#listaGrafo = {
#    '0': ['1', '4'],
#    '1': ['0', '2'],
#    '2': ['1', '5'],
#    '3': ['5'],
#    '4': ['0', '5'],
#    '5': ['2', '3', '4']
#}

#listaGrafo = {
#    '0': ['1', '2', '3'],
#    '1': ['4'],
#    '2': [],
#    '3': ['5'],
#    '4': [],
#    '5': []
#}


def DFS(visitado, listaGrafo, nodo):
    if nodo not in visitado:
        print (nodo, end=' ')
        visitado.append(nodo)

        random.shuffle(listaGrafo[nodo])

        for nodo in listaGrafo[nodo]:
            DFS(visitado, listaGrafo, nodo)

visitado = []
DFS(visitado, listaGrafo, '0')