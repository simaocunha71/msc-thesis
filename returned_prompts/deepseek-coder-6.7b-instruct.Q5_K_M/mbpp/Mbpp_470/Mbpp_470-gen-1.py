
def add_pairwise(t):
    return tuple(t[i] + t[i + 1] for i in range(len(t) - 1))

assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
"""

"""

