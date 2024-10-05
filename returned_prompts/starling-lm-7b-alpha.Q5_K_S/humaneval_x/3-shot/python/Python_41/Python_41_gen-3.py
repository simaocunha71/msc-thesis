    result = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            result += abs(i - j)

    return result


