from .edge import Edge
import heapq

class Graph:
    # Construtor da classe, cria uma lista vazia.
    def __init__(self):
        self.adjacency_list = {}

    # Adiciona um nó ao grafo.
    def add_vertex(self, vertex_id):
        if vertex_id not in self.adjacency_list:
            self.adjacency_list[vertex_id] = []

    # Adiciona uma aresta (u,v) ao grafo.
    def add_edge(self, u, v, weight, edge_id):
        # Cria arestas para as duas direções.
        edge1 = Edge(id=edge_id, to=v, weight=weight)
        edge2 = Edge(id=edge_id, to=u, weight=weight)
        
        # Adiciona aresta nas duas listas.
        self.adjacency_list[u].append(edge1)
        self.adjacency_list[v].append(edge2)

    # Faz a leitura completa do grafo.
    def read_graph(self):
        # Lê o tamanho do grafo (N vértices e M arestas).
        N, M = map(int, input().split())

        # Adiciona os N vértices.
        for i in range(N):
            self.add_vertex(i)

        # Adiciona as M arestas, com o i sendo o id de cada aresta.
        for i in range(1, M+1):
            u, v, weight = map(int, input().split())
            self.add_edge(u, v, weight, i)

    def dijkstra(self, u):
        # Inicializa os antecessores com -1 e as distâncias com infinito, menos o da origem.
        distances = {vertex: float('inf') for vertex in self.adjacency_list}
        distances[u] = 0
        
        # Heap começa com a tupla da origem.
        heap = [(0, u)] # (distância, id do vértice)
        
        # Vértices visitados, começa vazio.
        visited = set()

        while heap:
            # Remove o vértice com a menor distância.
            distance, vertex = heapq.heappop(heap)

            if vertex in visited:
                continue
        
            # Marca como visitado.
            visited.add(vertex)

            # Relaxa as arestas (processa os vizinhos)
            for edge in self.adjacency_list[vertex]:
                if edge.to not in visited:
                    new_distance = distance + edge.weight

                    # Se encontrou um caminho melhor, atualiza
                    if new_distance < distances[edge.to]:
                        distances[edge.to] = new_distance
                        heapq.heappush(heap, (new_distance, edge.to))
        
        # Retorna o dicionário com todas as distâncias. 
        return distances