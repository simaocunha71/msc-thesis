def multiply_elements(tup):
    N = len(tup) - 1
    result = []
    for i in range(N):
        result.append(tup[i] * tup[i+1])
    return tuple(result)