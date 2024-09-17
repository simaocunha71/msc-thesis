def multiply_elements(tup):
    result = []
    for i in range(len(tup)-1):
        result.append(tup[i] * tup[i+1])
    return tuple(result)