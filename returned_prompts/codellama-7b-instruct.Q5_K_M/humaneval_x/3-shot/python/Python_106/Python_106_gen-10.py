    result = [1] * n
    for i in range(1, n):
        if i % 2 == 0:
            result[i] = i
        else:
            result[i] = sum(range(1, i + 1))
    return result


