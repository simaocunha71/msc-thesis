def combinations_list(lst):
    if len(lst) == 0:
        return [[]]
    result = []
    for i, elem in enumerate(lst):
        for combination in combinations_list(lst[i+1:]):
            result.append([elem] + combination)
    return result