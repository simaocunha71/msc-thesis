    result = [n]
    for i in range(1, n):
        if n % 2 == 0:
            result.append(result[-1] + 2)
        else:
            result.append(result[-1] + 2)
    return result


