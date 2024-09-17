def add_pairwise(tuple):
    result = []
    for i in range(len(tuple)-1):
        result.append(tuple[i]+tuple[i+1])
    result.append(tuple[-1]+tuple[-2])
    return tuple(result)