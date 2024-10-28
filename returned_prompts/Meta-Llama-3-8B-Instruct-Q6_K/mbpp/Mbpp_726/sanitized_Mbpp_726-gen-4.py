def multiply_elements(tup):
    result = tuple()
    for i in range(len(tup) - 1):
        result += (tup[i] * tup[i+1],)
    return result