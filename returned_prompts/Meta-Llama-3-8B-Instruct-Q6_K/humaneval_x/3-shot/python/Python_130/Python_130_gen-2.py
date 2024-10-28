    if n == 0:
        return [3]

    if n == 1:
        return [3]

    if n == 2:
        return [3, 2]

    result = [3, 2]
    while len(result) < n + 1:
        next_val = result[-1] + result[-2] + result[-3]
        result.append(next_val)

    return result


