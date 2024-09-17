def multiply_elements(t):
    result = []
    for i in range(len(t) - 1):
        result.append(t[i] * t[i+1])
    return tuple(result)