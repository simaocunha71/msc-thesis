    if n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    elif n == 2:
        return [1, 3, 2, 8]

    result = [1, 3]
    a, b = 1, 3
    for _ in range(n - 2):
        result.append(a + b)
        a, b = b, a + b

    return result


