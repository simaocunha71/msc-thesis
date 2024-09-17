def combinations_list(lst):
    if len(lst) == 0:
        return [[]]
    if len(lst) == 1:
        return [lst]
    result = []
    for i in range(len(lst)):
        for sublist in combinations_list(lst[i+1:]):
            result.append([lst[i]] + sublist)
    return result