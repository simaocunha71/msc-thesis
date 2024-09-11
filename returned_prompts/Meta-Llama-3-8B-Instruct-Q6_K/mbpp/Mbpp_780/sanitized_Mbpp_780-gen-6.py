from itertools import product
def find_combinations(tups):
    return [(a, b) for a, b in product(tups, repeat=2) if a[0] + a[1] == b[0] + b[1]]