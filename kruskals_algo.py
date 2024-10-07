# Class to represent a disjoint set (Union-Find)
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# Kruskal's Algorithm to find MST
def kruskal(graph):
    edges = []
    n = len(graph)  # number of vertices
    # Convert the adjacency list to a list of edges (u, v, weight)
    for u in range(n):
        for v, weight in graph[u]:
            edges.append((weight, u, v))
    # Sort all edges by weight
    edges.sort()
    disjoint_set = DisjointSet(n)
    mst = []
    mst_weight = 0
    # Process each edge in increasing order of weight
    for weight, u, v in edges:
        # Check if the selected edge forms a cycle
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append((u, v, weight))
            mst_weight += weight
    return mst, mst_weight

# Function to take user input for adjacency list graph
def input_graph():
    graph = []
    n = int(input("Enter the number of vertices: "))
    print("Enter the adjacency list (vertex, weight) for each vertex (enter -1 to stop):")
    for i in range(n):
        edges = []
        while True:
            vertex, weight = map(int, input(f"Enter edge for vertex {i} (vertex weight): ").split())
            if vertex == -1:
                break
            edges.append((vertex, weight))
        graph.append(edges)

    return graph

# Example usage
graph = input_graph()

mst, total_weight = kruskal(graph)
print("\nMinimum Spanning Tree:")
for u, v, weight in mst:
    print(f"Edge {u} - {v}: {weight}")
print(f"Total weight of MST: {total_weight}")
