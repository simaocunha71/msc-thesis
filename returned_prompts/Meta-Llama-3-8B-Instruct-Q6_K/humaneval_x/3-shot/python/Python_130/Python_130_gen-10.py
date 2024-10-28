    if n == 0:
        return []
    elif n == 1:
        return [3]
    elif n == 2:
        return [3, 2]

    result = [3, 2]
    for i in range(2, n):
        if i % 2 == 0:
            result.append(1 + i / 2)
        else:
            result.append(result[i - 1] + result[i - 2] + result[i - 3])

    return result


