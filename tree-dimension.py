import networkx as nx
from itertools import combinations
from time import time
from networkx.algorithms.chordal import complete_to_chordal_graph


def minimal_triangulations(G):
    """Return all minimal triangulations of a graph

    Parameters
    ----------
    G : NetworkX graph
        Undirected graph

    Returns
    -------
    triangulations : List of NetworkX graphs
        List of all minimal triangulations of G
    """
    triangulations = []
    chords = set()
    if nx.is_chordal(G):
        triangulations.append(G.copy())
    else:
        H, alpha = complete_to_chordal_graph(G)
        for u, v in nx.complement(G).edges():
            if (u, v) not in chords:
                chords.add((u, v))
                T = G.copy()
                T.add_edge(u, v)
                triangulations.extend(minimal_triangulations(T))
    return triangulations


def median_dimension(G):
    if nx.is_chordal(G):
        return "The median-dimension is 1"
    else:
        triangulations = minimal_triangulations(G)
        L = []
        for t in triangulations:
            L.append(frozenset(t.edges()).difference(frozenset(G.edges())))
        for x in combinations(L, 2):
            if x[0] & x[1] == set():
                return "the dimension is 2"
