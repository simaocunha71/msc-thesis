import itertools
def combinations_colors(colors, n):
    return [tuple(x) for x in itertools.combinations(colors, n)]