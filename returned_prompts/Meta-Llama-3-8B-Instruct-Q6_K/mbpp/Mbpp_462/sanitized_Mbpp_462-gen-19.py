def combinations_list(lst):
    if not lst:
        return [ [] ]
    result = []
    for i, item in enumerate(lst):
        for combination in combinations_list(lst[:i] + lst[i+1:]):
            result.append([item] + combination)
    return result