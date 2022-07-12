from src.graph import Graph


class FloydWarshall:
    def __init__(self, graph: Graph, print_matrix=True):
        self.node_number = graph.count_nodes()

        self.matrix = [[float('inf') for u in graph.V.keys()] for v in graph.V.keys()]
        for index in range(self.node_number):
            self.matrix[index][index] = 0.0
        for edge in graph.A:
            self.matrix[int(edge.vi.index) - 1][int(edge.vf.index) - 1] = edge.weight
            self.matrix[int(edge.vf.index) - 1][int(edge.vi.index) - 1] = edge.weight

        self._fill_matrix()
        if print_matrix:
            self._print_matrix()

    def _fill_matrix(self):
        for v in range(self.node_number):
            for row in range(self.node_number):
                for column in range(self.node_number):
                    self.matrix[row][column] = min(
                        self.matrix[row][column], self.matrix[row][v] + self.matrix[v][column])

    def _print_matrix(self):
        for row in range(len(self.matrix)):
            line_print = "{}: ".format(row + 1)
            for col in range(len(self.matrix)):
                line_print += "{:.2f}, ".format(self.matrix[row][col])
            print(line_print[:-2])


if __name__ == "__main__":
    g = Graph("nets/teste_grafo_2.txt")
    FloydWarshall(g)
