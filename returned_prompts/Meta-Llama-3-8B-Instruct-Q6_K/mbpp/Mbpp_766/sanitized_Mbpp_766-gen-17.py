def pair_wise(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            result.append((lst[i], lst[j]))
    return result