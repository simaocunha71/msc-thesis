from itertools import combinations
from itertools import product
def find_combinations(t):
    c = []
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            c.append(tuple(t[i]+t[j]))
    return c