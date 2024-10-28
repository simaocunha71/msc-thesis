def combinations_list(lst):
    return list(itertools.chain.from_iterable(itertools.combinations(lst, i) for i in range(len(lst)+1)))

