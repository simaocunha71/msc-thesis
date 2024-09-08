def combinations_colors(lst, n):
    import itertools
    return list(itertools.product(*([lst]*n)))