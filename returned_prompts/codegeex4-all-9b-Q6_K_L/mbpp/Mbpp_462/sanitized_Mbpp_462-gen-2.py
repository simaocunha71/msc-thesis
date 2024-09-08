def combinations_list(lst):
    if not lst:
        return [[]]
    else:
        result = []
        for i in range(len(lst)):
            for combination in combinations_list(lst[:i] + lst[i+1:]):
                result.append([lst[i]] + combination)
        return result + [[]]