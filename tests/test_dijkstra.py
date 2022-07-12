import unittest

from src.graph import Graph
from src.breadth_first_search import BreadthFirstSearch


class BreadthFirstSearchTest(unittest.TestCase):
    def test_example_1_build_correct_levels(self):
        g = Graph('src/nets/teste_grafo.txt')
        bfs = BreadthFirstSearch(g, '1', print_levels=False)
        self.assertEqual(list(bfs.node_distance.values()), [0, 1, 1, 2, 2, 2, float('inf')])

    def test_example_2_build_correct_levels(self):
        g = Graph('src/nets/teste_grafo_2.txt')
        bfs = BreadthFirstSearch(g, '1', print_levels=False)
        self.assertEqual(list(bfs.node_distance.values()), [0, 1, 1, 2, 1, 2, 1, 2, 2, 2, 3, 3, 3, 4, 4])

