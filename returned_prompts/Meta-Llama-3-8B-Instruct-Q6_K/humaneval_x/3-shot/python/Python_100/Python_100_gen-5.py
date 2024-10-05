    result = [n]
    for _ in range(1, n):
        if n % 2 == 1:
            n += 1
        else:
            n += 2
        result.append(n)
    return result


