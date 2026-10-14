# Graph Definition
Adjacency_outgoing = {
    "A": 4,
    "B": 3,
    "C": 3,
    "D": 4,
    "E": 2,
    "F": 3,
    "G": 3,
    "H": 3,
    "I": 3,
    "J": 3,
    "K": 3,
    "L": 3,
    "M": 3,
    "N": 3,
    "O": 3,
    "P": 3,
    "Q": 3,
    "R": 3,
    "S": 3,
    "T": 3
}
Adjacency_incoming = {
    "A": ["C", "E", "H", "P", "T"],
    "B": ["A", "Q"],
    "C": ["A", "B", "D", "G", "R"],
    "D": ["A", "C", "I", "S"],
    "E": ["A", "D", "J", "T"],
    "F": ["B", "E", "K"],
    "G": ["B", "F", "H", "L"],
    "H": ["C", "F", "M"],
    "I": ["D", "G", "N"],
    "J": ["D", "I", "O"],
    "K": ["F", "J", "P"],
    "L": ["G", "K", "Q"],
    "M": ["H", "L", "R"],
    "N": ["I", "M", "S"],
    "O": ["J", "N", "T"],
    "P": ["K", "O"],
    "Q": ["L", "P"],
    "R": ["M", "Q"],
    "S": ["N", "R"],
    "T": ["O", "S"]
}

# pageRank
page_rank = {node: 1/len(Adjacency_outgoing) for node in Adjacency_outgoing}

# Difference Initialization
difference = 1

# Iterative pageRank
while difference > 0.0001:
    new_page_rank = {node: 0 for node in Adjacency_outgoing}
    for i in Adjacency_outgoing:
        for j in Adjacency_incoming[i]:
            new_page_rank[i] += page_rank[j]/Adjacency_outgoing[j]

    # Resetting Difference to Check for Convergence
    difference = 0
    for i in page_rank:
        difference += abs(page_rank[i] - new_page_rank[i])
    # print(difference)

    page_rank = new_page_rank.copy()

# Sort PageRank scores in ascending order
ranked_pages = sorted(page_rank.items(), key=lambda x: x[1])

print("\n===== PAGE RANKINGS =====")
for position, (page, score) in enumerate(ranked_pages, start=1):
    print(f"{position:2}. Page {page}: {score:.6f}")
