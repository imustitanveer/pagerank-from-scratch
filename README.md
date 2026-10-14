# PageRank From Scratch

A simple implementation of the **PageRank algorithm** in pure Python, built from scratch to explore graph algorithms, iterative computation, and convergence.

No external libraries. Just Python, dictionaries, and a little math.

## Overview

PageRank is a graph-based ranking algorithm originally developed by Google to measure the relative importance of webpages.

The central idea is simple:

> A page is important if other important pages link to it.

Rather than counting incoming links alone, PageRank considers the importance of the linking pages and how many outgoing links they have.

This project implements PageRank using an iterative approach, without relying on graph-processing libraries such as NetworkX.

## How It Works

### 1. Graph Representation

The graph is represented using two dictionaries:

- **Outgoing adjacency:** Stores the number of outgoing links for each node.
- **Incoming adjacency:** Stores the nodes linking to each node.

For example:

```python
Adjacency_outgoing = {
    "A": 2,
    "B": 1,
    "C": 1
}

Adjacency_incoming = {
    "A": ["C"],
    "B": ["A"],
    "C": ["A", "B"]
}
```

This represents the directed graph:

```text
A ──→ B
│     │
│     ▼
└───→ C
      │
      └──→ A
```

### 2. PageRank Formula

The standard PageRank equation is:

$$
PR(A) = \frac{1-d}{N} + d\sum_{i \rightarrow A}\frac{PR(i)}{L(i)}
$$

Where:

- **PR(A):** PageRank of page A.
- **d:** Damping factor.
- **N:** Total number of pages.
- **PR(i):** PageRank of a page linking to A.
- **L(i):** Number of outgoing links from page i.

For this implementation, the damping factor is set to **d = 1**, simplifying the equation to:

$$
PR(A) = \sum_{i \rightarrow A}\frac{PR(i)}{L(i)}
$$

Each node distributes its importance equally among the nodes it links to.

### 3. Initialization

Every node begins with an equal PageRank:

$$
PR(i) = \frac{1}{N}
$$

For a graph containing 20 nodes, each node starts with a rank of 0.05.

### 4. Iterative Calculation

The algorithm repeatedly:

1. Initializes a new set of PageRank scores.
2. Calculates each node's rank using incoming links.
3. Compares the new scores against the previous iteration.
4. Updates the PageRank values.
5. Repeats until convergence.

Previous and updated scores are stored separately to ensure that every calculation within an iteration uses the same set of values.

### 5. Convergence

Convergence is determined using the sum of absolute differences between consecutive iterations:

$$
\Delta = \sum_{i=1}^{N}|PR_{new}(i)-PR_{old}(i)|
$$

The algorithm stops when:

$$
\Delta < 0.0001
$$

This means the total change in PageRank scores between iterations has become sufficiently small.

## Example Results

The implementation was tested on a directed graph containing **20 nodes and 62 edges**.

The algorithm converged after **18 iterations**, reaching a final difference of approximately:

$$
\Delta = 8.96 \times 10^{-5}
$$

The five highest-ranked pages were:

| Rank | Page | PageRank |
|------|------|----------|
| 1 | A | 0.100128 |
| 2 | C | 0.086487 |
| 3 | D | 0.079683 |
| 4 | E | 0.068432 |
| 5 | G | 0.068196 |

The results demonstrate how importance propagates through a network based on incoming links and the relative importance of contributing nodes.

## Running the Project

### Requirements

- Python 3.10+
- No external dependencies

### Execution

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/pagerank-from-scratch.git
cd pagerank-from-scratch
```

Run the algorithm:

```bash
python pagerank.py
```

The program calculates PageRank scores until convergence and displays the resulting rankings.

## Complexity Analysis

Let:

- **V:** Number of vertices (pages).
- **E:** Number of directed edges (links).
- **K:** Number of iterations required for convergence.

Each iteration processes every vertex and its incoming edges.

**Time complexity per iteration:**

$$
O(V+E)
$$

**Total time complexity:**

$$
O(K(V+E))
$$

**Space complexity:**

$$
O(V+E)
$$

The graph representation requires space proportional to its vertices and edges, while the PageRank dictionaries require additional O(V) space.

## Limitations

This is an educational implementation of PageRank, not a production-ready search ranking system.

Current limitations include:

- **No damping factor:** Uses d = 1, which does not guarantee convergence for every graph.
- **No dangling-node handling:** Nodes without outgoing links are not explicitly handled.
- **No maximum iteration limit:** Certain graph structures may cause the algorithm to run indefinitely.
- **Static graph:** Graph connections are manually defined.

## Potential Improvements

- [ ] Introduce a configurable damping factor.
- [ ] Handle dangling nodes.
- [ ] Add a maximum iteration limit.
- [ ] Automatically generate incoming adjacency lists from outgoing connections.
- [ ] Support loading graphs from external files.
- [ ] Compare results against NetworkX's PageRank implementation.
- [ ] Visualize PageRank scores and graph relationships.

## Why I Built This

This project was built as part of my exploration of **Data Structures and Algorithms (DSA)**.

The goal was to understand PageRank at an algorithmic level rather than relying on an existing implementation.

Key concepts explored:

- Directed graphs and adjacency lists
- Dictionary-based graph representations
- Iterative algorithms
- Rank propagation
- Convergence detection
- Time and space complexity

The entire algorithm was implemented using standard Python.

## License

MIT License
