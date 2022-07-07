from src.graph import *


class HierHolzer:
    def __init__(self, g: Graph):
        self.g = g

    def search_euler_sub_cycle(self, g: Graph, v: Node, c: dict):
        cycle = [v]
        current_node = v
        first_iteration = True
        while current_node != v or first_iteration:
            non_visited_edge_attached_to_x_exists = False
            first_iteration = False
            edge = None
            for e in self.g.A:
                if ((e.vi == current_node) or (e.vf == current_node)) and (not c.get(e)):
                    non_visited_edge_attached_to_x_exists = True
                    edge = e
                    break
            if not non_visited_edge_attached_to_x_exists:
                return False, None
            else:
                c[edge] = True
                if current_node == edge.vi:
                    current_node = edge.vf
                elif current_node == edge.vf:
                    current_node = edge.vi
                else:
                    raise Exception("The current node is not one of the points connected by the edge")
                cycle.append(current_node)

        for e in self.g.A:
            if (e.vi in cycle) and (not c.get(e)):
                r, sub_cycle = self.search_euler_sub_cycle(g, e.vi, c)
                if not r:
                    return False, None
                node_index = cycle.index(e.vi)
                cycle = cycle[:node_index] + sub_cycle + cycle[node_index + 1:]
            elif (e.vf in cycle) and (not c.get(e)):
                r, sub_cycle = self.search_euler_sub_cycle(g, e.vf, c)
                if not r:
                    return False, None
                node_index = cycle.index(e.vf)
                cycle = cycle[:node_index] + sub_cycle + cycle[node_index + 1:]
        return True, cycle

    def hier_holzer(self):
        visited_edges = {a: False for a in self.g.A}
        chosen_node = 0
        for v in self.g.adjacency.keys():
            if self.g.adjacency[v]:
                chosen_node = v
                break
        r, cycle = self.search_euler_sub_cycle(self.g, chosen_node, visited_edges)
        if not r:
            return False, None

        else:
            if False in visited_edges.values():
                return False, None
            else:
                return True, cycle


if __name__ == "__main__":
    g1 = Graph('nets/teste_grafo_ciclo_euleriano_2.txt')
    hH1 = HierHolzer(g1)
    has_cycle, eu_cycle = hH1.hier_holzer()
    if has_cycle:
        cycle_string = ""
        for node in eu_cycle:
            cycle_string += " - " + node.label
        print(cycle_string[2:])
    else:
        print("There is no eulerian cycle on the current net")
