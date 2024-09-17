import itertools
def large_product(a, b, n):
    return sorted([i*j for i, j in itertools.product(a, b)], reverse=True)[:n]