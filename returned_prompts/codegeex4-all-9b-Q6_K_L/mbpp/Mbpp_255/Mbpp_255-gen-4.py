import itertools
def combinations_colors(colors, n):
    return list(itertools.combinations_with_replacement(colors, n))

