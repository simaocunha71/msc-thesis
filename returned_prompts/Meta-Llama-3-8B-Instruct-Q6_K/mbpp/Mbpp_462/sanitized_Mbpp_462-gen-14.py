def combinations_list(lst):
    import itertools
    result = []
    for r in range(len(lst) + 1):
        result.extend(itertools.combinations(lst, r))
    return [list(x) for x in result]