from .edge import Edge
import heapq

class Graph:
    # Construtor da classe, cria uma lista vazia e um dicionário de arestas para facilitar a busca.
    def __init__(self):
        self.adjacency_list = {}
        self.edges = {}

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

        # Adiciona a aresta ao dicionário de arestas.
        self.edges[edge_id] = (u, v, weight)

    # Faz a leitura completa do grafo.
    def read_graph(self):
        # Lê o tamanho do grafo (N vértices e M arestas).
        N, M = map(int, input().split())

        # Adiciona os N vértices.
        for i in range(1, N+1):
            self.add_vertex(i)

        # Adiciona as M arestas, com o i sendo o id de cada aresta.
        for i in range(1, M+1):
            u, v, weight = map(int, input().split())
            self.add_edge(u, v, weight, i)

    # Encontra aresta.
    def find_edge(self, edge_id):
        return self.edges[edge_id]
    
    # Remove aresta.
    def remove_edge(self, edge_id):
        if edge_id not in self.edges:
            return

        # Obtém os vértices da aresta.
        u, v, weight = self.find_edge(edge_id) 
        
        # Remove da lista de adjacência de u (Filtra arestas com esse id).
        self.adjacency_list[u] = [edge for edge in self.adjacency_list[u] if edge.id != edge_id]
        
        # Remove da lista de adjacência de v.
        self.adjacency_list[v] = [edge for edge in self.adjacency_list[v] if edge.id != edge_id]
        
        # Remove do dicionário
        del self.edges[edge_id]

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
    
    # Encontra arestas presentes em pelo menos um caminho mais curto.
    def find_edges_in_shortest_paths(self, u, v):
        # Calcula as distâncias mínimas saindo de u e de v.
        u_distances = self.dijkstra(u)
        v_distances = self.dijkstra(v)

        # Distância mínima entre u e v.
        u_and_v_distance = u_distances[v]

        # Cria set para armazenar as arestas presentes em pelo menos 1 caminho mínimo.
        min_edges = set()

        # Cria set de arestas visitadas (por ID), para otimizar o algoritmo.
        visited = set()

        for vertex in self.adjacency_list:
            for edge in self.adjacency_list[vertex]:

                # Verifica se aresta já foi checada.
                if edge.id in visited:
                    continue
                
                # Marca como visitada.
                visited.add(edge.id)
                
                # Verifica se a aresta está em um caminho mínimo.
                if u_distances[vertex] + edge.weight + v_distances[edge.to] == u_and_v_distance:
                    min_edges.add(edge.id)
        
        # Retorna set ordenada dos IDs.
        return sorted(set(min_edges))