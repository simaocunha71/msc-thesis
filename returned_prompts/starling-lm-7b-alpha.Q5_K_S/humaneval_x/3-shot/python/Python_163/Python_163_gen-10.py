    result = []
    if a % 2 == 0:
        result.append(a)
    for x in range(a + 1, b):
        if x % 2 == 0:
            result.append(x)
    if b % 2 == 0:
        result.append(b)
    return result


