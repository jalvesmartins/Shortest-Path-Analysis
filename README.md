# Shortest Path Analysis - Dijkstra's Algorithm

## Problem Description

This project analyzes shortest paths in weighted graphs using Dijkstra's algorithm. Given a graph with N vertices and M weighted edges, the program solves three main problems:

1. **Part 1**: Find the shortest distance from vertex 1 to vertex N
2. **Part 2**: Identify all edges that belong to at least one shortest path from vertex 1 to N
3. **Part 3**: Identify critical edges - edges whose removal would increase the shortest distance between vertices 1 and N

The problem is modeled as follows:
- Input: N vertices (1 to N) and M weighted edges
- Output: Three parts showing distance, edges in shortest paths, and critical edges

## Solution Approach

The solution implements **Dijkstra's algorithm** to efficiently find shortest paths in weighted graphs. The implementation uses:

- **Min-Heap Priority Queue**: For efficient vertex selection during Dijkstra's execution
- **Bidirectional Distance Calculation**: Computing distances from both source and destination
- **Path Counting**: Dynamic programming approach to count the number of shortest paths
- **Edge Analysis**: Identifying edges that participate in shortest paths and determining criticality

For detailed information about the algorithm implementation and complexity analysis, refer to the documentation in the `docs/` folder.

## How to Run

### Prerequisites

- Python 3.6 or higher
- Standard library only (no external dependencies)

### Running the Program

Execute the main program with input from stdin:

```bash
python3 main.py < data/input/in1
```

Or use any of the available test inputs:

```bash
python3 main.py < data/input/in2
python3 main.py < data/input/in3
```

Or pipe input directly:

```bash
echo "4 5
1 2 1
2 3 2
1 3 4
3 4 1
2 4 5" | python3 main.py
```

### Input Format

```
N M
U1 V1 W1
U2 V2 W2
...
UM VM WM
```

Where:
- N: number of vertices (vertices are numbered from 1 to N)
- M: number of edges
- Ui, Vi: vertices connected by edge i (1 ≤ Ui, Vi ≤ N)
- Wi: weight of edge i (positive integer)

### Output Format

```
Parte 1: X
Parte 2: E1 E2 E3 ... Ek
Parte 3: C1 C2 C3 ... Cm
```

Where:
- **Part 1 (X)**: Shortest distance from vertex 1 to vertex N
- **Part 2 (E1, E2, ...)**: IDs of edges that belong to at least one shortest path (sorted)
- **Part 3 (C1, C2, ...)**: IDs of critical edges (sorted), or -1 if no critical edges exist

### Test Cases

The repository includes test cases in the `data/input/` directory:

```bash
# Run all tests
for test in data/input/in*; do
    echo "Testing: $test"
    python3 main.py < "$test"
    echo "---"
done
```

## Project Structure

```
.
├── main.py                 # Main executable file
├── src/
│   └── graph/
│       ├── graph.py        # Graph data structure with adjacency list
│       ├── edge.py         # Edge class definition
│       └── __init__.py
├── data/                   # Test cases
│   ├── input/
│   │   ├── in1
│   │   ├── in2
│   │   └── in3
│   └── output/
│       ├── out1
│       ├── out2
│       └── out3
├── docs/                   # Documentation
│   └── doc_tp1.pdf
├── vpl/
│   └── tp1.py
└── README.md
```

## Implementation Details

### Graph Class (`src/graph/graph.py`)

The `Graph` class provides the following key methods:

- **`read_graph()`**: Reads graph input and builds adjacency list representation
- **`dijkstra(u)`**: Computes shortest distances from vertex u to all other vertices
- **`find_edges_in_shortest_paths(u, v)`**: Identifies edges in at least one shortest path
- **`count_paths(u)`**: Counts the number of shortest paths from u to all vertices
- **`find_critical_edges(u, v)`**: Identifies critical edges between vertices u and v

### Edge Class (`src/graph/edge.py`)

Simple data structure representing a directed edge with:
- `id`: unique identifier for the edge
- `to`: destination vertex
- `weight`: edge weight

### Algorithm Complexity

- **Dijkstra's Algorithm**: O((N + M) log N) using min-heap
- **Edge Analysis**: O(M) for checking each edge
- **Path Counting**: O(N + M) using topological order based on distances
- **Overall Complexity**: O((N + M) log N)

## Author

João Henrique Alves Martins  
Universidade Federal de Minas Gerais (UFMG)  
jalvesmartins16@ufmg.br
