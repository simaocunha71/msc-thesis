def combinations_list(lst):
    result = []
    for i in range(len(lst)+1):
        for comb in itertools.combinations(lst, i):
            result.append(list(comb))
    return result