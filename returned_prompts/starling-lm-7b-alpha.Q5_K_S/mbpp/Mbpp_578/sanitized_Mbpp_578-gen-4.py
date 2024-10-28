import itertools
def interleave_lists(a, b, c):
    return list(itertools.chain(a, b, c))