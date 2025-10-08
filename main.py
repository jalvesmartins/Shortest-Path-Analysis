from src.graph import Graph

def main():
    g = Graph()
    g.read_graph()

    # Parte 1.
    distances = g.dijkstra(1)
    N = max(g.adjacency_list.keys())
    print(f"Parte 1: {distances[N]}")

    # Parte 2: Arestas em pelo menos 1 caminho mínimo.
    min_edges = g.find_edges_in_shortest_paths(1, N)
    print(f"Parte 2: {' '.join(map(str, min_edges))}")

    # Parte 3: Arestas críticas.
    critical_edges = g.find_critical_edges(1, N)
    print(f"Parte 3: {' '.join(map(str, critical_edges))}")

if __name__ == "__main__":
    main()