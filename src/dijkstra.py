from src.graph import *


class Dijkstra:
    def __init__(self, g: Graph, first_index: str, print_distances=True):
        self.visited = set()
        self.nodes_info = dict()
        self.g = g
        self.first_index = first_index

        for key in g.V.keys():
            self.nodes_info[key] = {
                'distance': float('inf'),
                'predecessor': None
            }

        self.nodes_info[self.first_index] = {
            'distance': 0,
            'predecessor': None
        }
        self.explore()
        if print_distances:
            self.print_distances()

    def explore(self):
        while len(self.visited) != len(self.g.V.values()):
            u = min([v for v in self.g.V.values() if v.index not in self.visited],
                    key=lambda node: self.nodes_info[node.index].get('distance'))
            self.visited.add(u.index)

            for v in [node for node in self.g.neighbors(u) if node.index not in self.visited]:
                if self.nodes_info.get(v.index).get('distance') > self.nodes_info.get(u.index).get('distance') + \
                        self.g.weight(u, v):
                    self.nodes_info.get(v.index)['distance'] = self.nodes_info.get(u.index).get('distance') + \
                                                               self.g.weight(u, v)
                    self.nodes_info.get(v.index)['predecessor'] = u

    def print_distances(self):
        for v in self.g.V.keys():
            path = []
            peso = self.nodes_info.get(v).get('distance')
            if peso != float('inf'):
                current_node = v
                first_node = self.first_index
                while current_node != first_node:
                    path.append(current_node)
                    current_node = self.nodes_info[current_node]['predecessor'].index
                path.append(first_node)

            path.reverse()

            print("{}: {}; d={}".format(v, path, peso))


if __name__ == "__main__":
    dk = Dijkstra(Graph('nets/teste_grafo_2.txt'), '1')
