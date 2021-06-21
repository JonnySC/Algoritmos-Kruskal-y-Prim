import networkx as nx
import numpy as n

def Prim(G = nx.Graph(), R = None):
   # Q es la lista de vértices que no están en el árbol
    Q    = {}
   # Q es la lista de vértices que no están en el árbol
    pred = {}

    # Inicializamos Q con todos los vértices con valor infinito, porque en este
    # señala que todavía no hay conexión entre ningún vértice. Asimismo, ninguno
    # el vértice tiene un ancestro, por lo que usamos el valor 'nulo'.
    for v,data in G.nodes(data=True):
        Q[v]    = n.inf
        pred[v] = 'null'

    # Si no hay pesos definidos para los vértices, asignamos el valor 1.0.
    # Este es un enfoque alternativo al que usamos en Kruskal, de usar un 19 
    # variable para comprobar si estamos teniendo en cuenta el peso o no.
    for e,x in G.edges():
        if ('weight' not in G[e][x]):
            G[e][x]['weight'] = 1.0

    # Inicializamos la raíz del árbol con un valor de 0 y creamos un árbol llamado 25 
    # MST con vértices G solamente.
    Q[R] = 0.0
    MST  = nx.create_empty_copy(G)

    while Q:
        # u: = índice del elemento más pequeño de Q 31 
        # porque queremos el vértice más ligero
        u = min(Q,key=Q.get)

        # eliminado de Q ya que se agregará al árbol
        del Q[u]

        # mantenemos los pesos mínimos de cada vecino de u en Q, si son 38 
        # más pequeños que los que ya están almacenados
        for vecino in G[u]:
            if vecino in Q:
                if G[u][vecino]['weight'] < Q[vecino]:
                    pred[vecino] = u
                    Q[vecino]    = G[u][vecino]['weight']

        # Si hay predecesores de u, agregaremos los bordes 46 
        # conectando el vértice u con sus predecesores
        if pred[u] is not 'null':
            for v1,v2,data in G.edges(data=True):
                # para preservar los datos de los bordes, necesitábamos este bucle 50 
                # que verifica todos los bordes del gráfico y busca el borde 51 
                # (pred (u), u), sin embargo, como un gráfico no dirigido de la biblioteca 52 
                # no duplica el existencia de sus aristas en el 53 
                # conjunto de aristas, es decir, si tiene (u, v) no tiene (v, u), hay una 54 
                # necesidad de verificar, en el caso de grafos no dirigidos, 55 
                # si hay del borde (u, pred (u)) en lugar de 56 # (pred (u), u)
                if ( v1 is pred[u] and v2 is u ):
                    MST.add_edge(pred[u],u,data)
                elif (  ( v1 is u and v2 is pred[u] ) and
                        ( not nx.is_directed(G) )  ):
                    MST.add_edge(pred[u],u,data)

    return MST
