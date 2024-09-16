import itertools
def combinations_colors(colors,length):
    return [tuple(x) for x in itertools.combinations(colors,length)]