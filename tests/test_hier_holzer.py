import unittest

from src.graph import Graph
from src.hier_holzer import HierHolzer


class HierHolzerTests(unittest.TestCase):
    def test_koenigsberger_bruecken_no_cycle(self):
        g1 = Graph('src/nets/eulerian_cycle_koenigsberger_bruecken.txt')
        hh1 = HierHolzer(g1)
        has_cycle, eu_cycle = hh1.hier_holzer()
        self.assertFalse(has_cycle)

    def test_eulerian_cycle_indicate_correct_cycle(self):
        g1 = Graph('src/nets/teste_grafo_ciclo_euleriano_2.txt')
        hh1 = HierHolzer(g1)
        has_cycle, eu_cycle = hh1.hier_holzer()
        self.assertTrue(has_cycle)
        cycle_string = ""
        for node in eu_cycle:
            cycle_string += " - " + node.label
        self.assertEqual(cycle_string[3:], 'A - F - E - A - H - G - A - J - I - A - B - C - K - L - C - D - A')

