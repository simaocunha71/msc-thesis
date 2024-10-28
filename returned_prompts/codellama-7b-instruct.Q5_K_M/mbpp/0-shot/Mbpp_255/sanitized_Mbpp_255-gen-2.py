import itertools
def combinations_colors(colors,n):
    return [tuple(i) for i in itertools.combinations(colors,n)]