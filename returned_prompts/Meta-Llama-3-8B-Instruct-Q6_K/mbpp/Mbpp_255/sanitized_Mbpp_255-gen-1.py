from itertools import product
def combinations_colors(lst, n):
    return list(product(lst, repeat=n))