def combinations_list(lst):
    if not lst:
        return [[]]
    result = []
    for i in range(len(lst)):
        current = lst[i]
        rest = lst[:i] + lst[i+1:]
        for p in combinations_list(rest):
            result.append([current] + p)
    return result