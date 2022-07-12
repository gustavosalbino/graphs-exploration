from typing import Union
from random import randint
from typing import List


class Node:
    def __init__(self, ind: str, rot: str):
        self.index = ind
        self.label = rot

    def get_label(self) -> str:
        return self.label


class Edge:
    def __init__(self, vi: Node, vf: Node, weight: float):
        self.vi = vi
        self.vf = vf
        self.weight = weight


class Graph:
    def __init__(self, file_path: str, directed=False):
        self.adjacency = {}
        self.V = dict()
        self.A = []
        self.directed = directed

        self._read_net(file_path)
        self._create_adjacency()

    def _read_net(self, file_path):
        with open(file_path, 'r') as f:
            for line in f:
                if '*vertices' in line:
                    reading_nodes = True
                elif '*edges' in line:
                    reading_nodes = False
                elif '*arcs' in line:
                    reading_nodes = False
                    self.directed = True
                elif reading_nodes:
                    split = line.split(' ', 1)
                    last = split[-1]
                    if last[-1] == '\n':
                        last = last[:-1]
                    self.V.update({split[0]: Node(split[0], last)})
                else:
                    split = line.split()
                    self.A.append(Edge(self.V.get(split[0]), self.V.get(split[1]), float(split[2])))

    def _create_adjacency(self):
        for v in self.V.values():
            self.adjacency[v] = []
        for a in self.A:
            self.adjacency[a.vi].append([a.vf, a.weight])
            if not self.directed:
                self.adjacency[a.vf].append([a.vi, a.weight])

    def count_nodes(self) -> int:
        return len(self.V)

    def count_edges(self) -> int:
        return len(self.A)

    def degree(self, v: Node) -> int:
        return len(self.adjacency[v])

    def neighbors(self, v: Node) -> List[Node]:
        return [adjacency[0] for adjacency in self.adjacency[v]]

    def has_edge(self, u: Node, v: Node) -> bool:
        for adj in self.adjacency[u]:
            if adj[0] == v:
                return True
        return False

    def get_edge(self, u: Node, v: Node) -> Union[Edge, bool]:
        for a in self.A:
            if u == a.vi:
                if v == a.vf:
                    return a
        return False

    def weight(self, u: Node, v: Node) -> float:
        for adj in self.adjacency[u]:
            if adj[0] == v:
                return adj[1]
        return float('inf')


if __name__ == "__main__":
    g1 = Graph('nets/teste_grafo.txt')

    index1, index2 = 0, 0
    while index1 == index2:
        index1 = str(randint(1, 6))
        index2 = str(randint(1, 6))
    print(index1, index2)
    chosen_v = g1.V.get(index1)
    chosen_u = g1.V.get(index2)
    print('Label of chosen node V: ', chosen_v.get_label())
    print('Label of chosen node U: ', chosen_u.get_label())
    print('Number of nodes: ', g1.count_nodes())
    print('Number of edges: ', g1.count_edges())
    print('Has an edge between V and U: ', g1.has_edge(chosen_v, chosen_u))
    print('Degree of V: ', g1.degree(chosen_v))
    print('Degree of U: ', g1.degree(chosen_u))
    print('Neighbors of V: ', [viz.label for viz in g1.neighbors(chosen_v)])
    print('Neighbors of U: ', [viz.label for viz in g1.neighbors(chosen_u)])
    print('Weight of the edge V -> U: ', g1.weight(chosen_v, chosen_u))
