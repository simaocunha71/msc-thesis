    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i * f(i - 1))
        else:
            result.append(sum([j for j in range(1, i + 1)]))

    return result


