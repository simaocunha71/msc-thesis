def combinations_list(lst):
    if len(lst) == 0:
        return [[]]
    result = []
    for i, item in enumerate(lst):
        rest = lst[i+1:]
        for p in combinations_list(rest):
            result.append([item] + p)
    return result