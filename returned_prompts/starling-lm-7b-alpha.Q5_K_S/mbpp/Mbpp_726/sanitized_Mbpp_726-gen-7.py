def multiply_elements(t):
    res = []
    for i in range(len(t) - 1):
        res.append(t[i] * t[i + 1])
    return tuple(res)