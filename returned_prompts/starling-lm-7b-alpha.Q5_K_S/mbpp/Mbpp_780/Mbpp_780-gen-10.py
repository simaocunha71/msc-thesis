from itertools import combinations
from itertools import product

def find_combinations(t):
    c = []
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            c.append(tuple(t[i]+t[j]))
    return c

print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]))


"""
def find_combinations(t):
    c = []
    for i in product(t, repeat=2):
        c.append(tuple(i))
    return c
"""

"""
def find_combinations(t):
    c = []
    for i in combinations(t, 2):
        c.append(tuple(i))
    return c
"""

"""
def find_combinations(t):
    c = []
    for i in range(len(t)):
        for j in range(i, len(t)):
            c.append(tuple(t[i]+t[j]))
    return c
"""

"""
def find_combinations(t):
    c = []
    for i in range(len(t)):
        for j in range(i, len(t)):
            c.append((t[i][0]+t[j][0], t[i][1]+t[j][1]))
    return c
"""

"""
def find_combinations(t):
    c = []
    for i in range(len(t)):
        for j in range(i, len(t)):
            c.append((t[i][0]+t[j][0], t[i][1]+t[j][1]))
    return c
"""

"""
def find_combinations(t):
    c = []
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            c.append((t[i][0]+t[j][0], t[i][1]+t[j][1]))
    return c
"""

"""
def find_combin