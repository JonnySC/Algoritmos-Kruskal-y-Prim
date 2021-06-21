import networkx as nx

# Función auxiliar para encontrar el índice del conjunto donde está el vértice 4 
def encontrar_conjunto(lista, vertice):
    i = 0
    for conjunto in lista:
        if (vertice in conjunto):
            return i
        i = i+1

def Kruskal(G):
    if 'weight' in G.edges(data=True)[0][2]:
        grafo_com_peso = True
    else:
        grafo_com_peso = False

    MST = nx.create_empty_copy(G)

    if grafo_com_peso:
        E = sorted(G.edges(data=True), key=lambda k: k[2]['weight'])
    else:
        E = G.edges(data=True)

    vertices_conexos = []

    # creamos una lista de conjuntos disjuntos con solo un vértice cada uno, el 27 
    # comienzo, para que podamos hacer las uniones más tarde
    for v in G.nodes():
        vertices_conexos.append({v})

    for arista in E:
        indexConj1 = encontrar_conjunto(vertices_conexos, arista[0])
        indexConj2 = encontrar_conjunto(vertices_conexos, arista[1])

        # Si el conjunto encontrado para el vértice 0 es el mismo que el del vértice 1, 36 
        # para que no podamos unirlos, ya que esto cerraría un ciclo.
        if indexConj1 != indexConj2:

            # Si la gráfica contiene el peso, agregamos las tres piezas de información 40 
            # de borde (2 vértices y dados)
            if grafo_com_peso:
                MST.add_edge(arista[0], arista[1], arista[2])
            else:
                MST.add_edge(arista[0], arista[1])

            # eliminamos los dos conjuntos de vértices del vector vertices_connected
            if indexConj1 > indexConj2:
                conj1 = vertices_conexos.pop(indexConj1)
                conj2 = vertices_conexos.pop(indexConj2)
            else:
                conj2 = vertices_conexos.pop(indexConj2)
                conj1 = vertices_conexos.pop(indexConj1)

            # e inserte un nuevo conjunto de la unión de los dos
            vertices_conexos.append(conj1.union(conj2))

    return MST
