def f(n):
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(i * (i - 1) * (i - 2) * ... * 2 * 1)
        else:
            result.append(sum(range(1, i + 1)))
    return result



