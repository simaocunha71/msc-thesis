def combinations_list(lst):
    result = []
    for i in range(2**len(lst)):
        combo = [lst[j] for j in range(len(lst)) if (i & (1 << j)) != 0]
        result.append(combo)
    return result