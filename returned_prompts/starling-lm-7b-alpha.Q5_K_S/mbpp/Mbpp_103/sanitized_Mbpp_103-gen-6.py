from itertools import permutations
from itertools import combinations
def eulerian_num(n, m):
    # Create all permutations of numbers from 0 to n-1, and
    # choose m of them to be part of the Eulerian path
    p = list(permutations(range(n), m))
    # For each permutation, create a graph with a weight of 1 on each edge
    # Then, check if the graph contains an Eulerian path
    for perm in p:
        g = nx.Graph()
        for i in range(len(perm)):
            g.add_edge(perm[i-1], perm[i])
        if nx.is_eulerian(g):
            return True
    # If no permutation results in an Eulerian graph, the original graph has no Eulerian path
    return False