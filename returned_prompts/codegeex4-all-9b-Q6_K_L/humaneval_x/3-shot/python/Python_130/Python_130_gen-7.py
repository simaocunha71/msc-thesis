    if n == 0:
        return [1]
    if n == 1:
        return [1, 3]
    if n == 2:
        return [1, 3, 2]

    result = [1, 3, 2]

    for i in range(3, n + 1):
        if i % 2 == 0:
            result.append(1 + i / 2)
        else:
            result.append(result[-1] + result[-2] + result[-3])

    return result

