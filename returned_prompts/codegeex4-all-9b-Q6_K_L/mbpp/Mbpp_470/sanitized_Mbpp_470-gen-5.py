def add_pairwise(lst):
    result = []
    for i in range(len(lst) - 1):
        result.append(lst[i] + lst[i + 1])
    return tuple(result)