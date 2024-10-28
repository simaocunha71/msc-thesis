import itertools
def combinations_colors(colors,length):
    return [tuple(colors[i] for i in combination) for combination in itertools.combinations_with_replacement(range(len(colors)),length)]
