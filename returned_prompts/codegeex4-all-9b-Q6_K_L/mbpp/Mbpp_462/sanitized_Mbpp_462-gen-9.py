def combinations_list(lst):
    result = []
    for i in range(len(lst) + 1):
        for subset in itertools.combinations(lst, i):
            result.append(subset)
    return result