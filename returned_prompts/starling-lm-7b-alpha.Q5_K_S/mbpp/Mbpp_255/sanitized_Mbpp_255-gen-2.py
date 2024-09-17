def combinations_colors(colors,n):
    from itertools import product
    return list(product(colors, repeat=n))