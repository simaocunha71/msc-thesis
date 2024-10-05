    result = [0, 0, 2]
    while len(result) <= n:
        result.append(result[-1] + result[-2] + result[-3] + result[-4])
    return result[n]


