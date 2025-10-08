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
                
                # Verifica se a aresta está em um caminho mínimo (direção vertex → edge.to).
                if u_distances[vertex] + edge.weight + v_distances[edge.to] == u_and_v_distance:
                    min_edges.add(edge.id)
                # Verifica também a direção oposta (edge.to → vertex).
                elif u_distances[edge.to] + edge.weight + v_distances[vertex] == u_and_v_distance:
                    min_edges.add(edge.id)
        
        # Retorna set ordenada dos IDs.
        return sorted(min_edges)
    
    # Encontra o número de caminhos mínimos entre u e outros vértices.
    def count_paths(self, u):
        # Inicializa os contador com 0.
        path_count = {vertex: 0 for vertex in self.adjacency_list}

        # Inicializa o da origem com 1.
        path_count[u] = 1

        # Ordena as distâncias.
        distances = self.dijkstra(u)
        sorted_vertices = sorted(distances.keys(), key=lambda vertex: distances[vertex])

        for vertex in sorted_vertices:
            for edge in self.adjacency_list[vertex]:
                # Se aresta está em caminho mínimo.
                if distances[vertex] + edge.weight == distances[edge.to]:
                    # Adiciona os caminhos de u ao contador do vértice v, sendo que (u -> v).
                    path_count[edge.to] += path_count[vertex]
    
        return path_count
    
    # Encontra arestas que caso retiradas do grafo, aumentariam a distância entre os vértices u e v.
    def find_critical_edges(self, u, v):
        # Calcula arestas presentes em caminhos mínimos.
        candidate_edges = self.find_edges_in_shortest_paths(u, v)
        
        # Se não há arestas em caminhos mínimos, retorna -1.
        if not candidate_edges:
            return [-1]
        
        # Calcula distâncias da origem e do destino.
        u_distances = self.dijkstra(u)
        v_distances = self.dijkstra(v)

        # Menor caminho entre u e v.
        shortest_path = u_distances[v]

        # Encontra o número de caminhos mínimos (ida e volta).
        paths_forward = self.count_paths(u)
        paths_backward = self.count_paths(v)

        # Total de caminhos mínimos.
        total_paths = paths_forward[v]

        # Lista de críticos inicialmente vazia.
        critical = []
    
        for edge_id in candidate_edges:
            # Obtém os vértices da aresta.
            edge_1, edge_2, weight = self.find_edge(edge_id)
            
            if total_paths > 0:
                # Testa edge_1 -> edge_2 (Como não sabemos em qual ordem esta armazenado).
                if u_distances[edge_1] + weight + v_distances[edge_2] == shortest_path:
                    # Verifica se todos os caminhos passam por essa direção
                    if paths_forward[edge_1] * paths_backward[edge_2] == total_paths:
                        critical.append(edge_id)
                
                # Testa edge_2 -> edge_1.
                elif u_distances[edge_2] + weight + v_distances[edge_1] == shortest_path:
                    # Verifica se todos os caminhos passam por essa direção
                    if paths_forward[edge_2] * paths_backward[edge_1] == total_paths:
                        critical.append(edge_id)

        # Se nenhuma aresta é crítica, retorna -1.
        if len(critical) == 0:
            return [-1]

        return sorted(critical)