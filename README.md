# TP1 - Algoritmos 1
## Análise de Mobilidade Urbana com Grafos

### 📋 Descrição

Este projeto implementa soluções computacionais para três problemas de mobilidade urbana na cidade fictícia de Somatório, utilizando algoritmos de grafos para análise de rotas e identificação de pontos críticos no trânsito. O objetivo é determinar a melhor forma de implementar áreas verdes com menor impacto no tráfego.

### 🎯 Problemas Resolvidos

**Problema 1: Distância Mínima**
- Calcula a menor distância entre a entrada (vértice 1) e a saída (vértice N) da cidade

**Problema 2: Arestas em Caminhos Mínimos**
- Identifica todas as ruas (arestas) que aparecem em pelo menos um caminho mínimo
- Essas ruas são candidatas para implementação de áreas verdes

**Problema 3: Arestas Críticas**
- Identifica ruas que aparecem em TODOS os caminhos mínimos
- A remoção dessas ruas aumentaria necessariamente a distância mínima
- São pontos críticos do sistema viário

### 🛠️ Tecnologias

- **Linguagem:** Python 3
- **Estrutura de Dados:** Lista de adjacências
- **Algoritmos:** Dijkstra, Programação Dinâmica
- **Bibliotecas:** heapq (fila de prioridades)

### 📁 Estrutura do Projeto

```
tp1/
├── src/
│   └── graph/
│       ├── __init__.py
│       ├── edge.py          # Classe Edge
│       └── graph.py         # Classe Graph com algoritmos
├── vpl/
│   └── tp1.py              # Arquivo único para submissão VPL
├── data/
│   └── large_input/        # Casos de teste
│       ├── inp_large/
│       └── out_large/
├── docs/
│   └── instructions.pdf    # Especificação do trabalho
├── main.py                 # Arquivo principal
└── README.md
```

### 🚀 Como Executar

#### Opção 1: Usando o arquivo modular
```bash
python main.py
```

#### Opção 2: Usando o arquivo único (VPL)
```bash
python vpl/tp1.py
```

#### Com arquivo de entrada
```bash
cat data/large_input/inp_large/in1 | python main.py
```

### 📝 Formato de Entrada

```
N M
u1 v1 w1
u2 v2 w2
...
uM vM wM
```

Onde:
- `N`: número de vértices
- `M`: número de arestas
- `ui vi wi`: aresta i conectando vértices ui e vi com peso wi

### 📤 Formato de Saída

```
Parte 1: <distância mínima>
Parte 2: <lista de IDs das arestas em caminhos mínimos>
Parte 3: <lista de IDs das arestas críticas ou -1>
```

### 💡 Exemplo

**Entrada:**
```
6 7
1 2 1
2 3 1
3 6 1
1 4 2
4 5 2
5 6 2
2 5 3
```

**Saída:**
```
Parte 1: 3
Parte 2: 1 2 3
Parte 3: 1 2 3
```

### ⚙️ Complexidade

- **Problema 1:** O((V + E) log V)
- **Problema 2:** O(E log V + E)
- **Problema 3:** O(E log V + E)
- **Espaço:** O(V + E) para todos os problemas

### 🧪 Testes

Execute os casos de teste fornecidos:

```bash
# Teste 1
cat data/large_input/inp_large/in1 | python main.py

# Verificar saída esperada
cat data/large_input/out_large/out1
```

### 👨‍💻 Info

João Alves Martins
- Universidade Federal de Minas Gerais (UFMG)
- Disciplina: Algoritmos 1