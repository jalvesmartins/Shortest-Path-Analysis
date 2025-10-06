from .edge import Edge

class Graph:
    # Construtor da classe, cria uma lista vazia.
    def __init__(self):
        self.adjacency_list = {}

    # Adiciona um nó ao grafo.
    def add_vertex(self, vertex_id):
        if vertex_id not in self.adjacency_list:
            self.adjacency_list[vertex_id] = []

    # Adiciona uma aresta ao grafo.
    def add_edge(self, u, v, weight, edge_id):
        edge = Edge(id=edge_id, to=v, weight=weight)
        self.adjacency_list[u].append(edge)