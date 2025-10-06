class Edge:
    # Construtor da classe, recebe id, nó de destino e peso.
    def __init__(self, id, to, weight):
        self.id = id
        self.to = to # "Destino da aresta", a origem é armazenada na lita de adjacência.
        self.weight = weight

    # Função para facilitar o print da aresta.
    def __repr__(self):
        return f" self.id"