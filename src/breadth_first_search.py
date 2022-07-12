from src.graph import *


class BreadthFirstSearch:
    def __init__(self, g: Graph, first_index: str, print_levels=True):
        self.first_node = g.V.get(first_index)
        self.node_visited = {v.index: False for v in g.V.values()}
        self.node_distance = {v.index: float('inf') for v in g.V.values()}
        self.node_predecessor = {v.index: None for v in g.V.values()}

        self.node_visited[first_index] = True
        self.node_distance[first_index] = 0

        self.open_nodes = [self.first_node]

        self._explore(g)
        if print_levels:
            self._print_tree_levels(g)

    def _explore(self, g: Graph):
        while self.open_nodes:
            current_node = self.open_nodes.pop(0)
            for n in g.neighbors(current_node):
                if not self.node_visited.get(n.index):
                    self.node_visited[n.index] = True
                    self.node_distance[n.index] = self.node_distance.get(current_node.index) + 1
                    self.node_predecessor[n.index] = current_node
                    self.open_nodes.append(n)

    def _print_tree_levels(self, g: Graph):
        i = -1
        while True:
            i += 1
            level = [k for k in self.node_distance.keys() if self.node_distance.get(k) == i]
            if level:
                level_string = "{}: ".format(i)
                for n in level:
                    level_string += "{}, ".format(g.V.get(n).label)
                print(level_string[:-2])
            else:
                break


if __name__ == "__main__":
    graph = Graph('nets/teste_grafo_2.txt')
    BreadthFirstSearch(graph, '1')
