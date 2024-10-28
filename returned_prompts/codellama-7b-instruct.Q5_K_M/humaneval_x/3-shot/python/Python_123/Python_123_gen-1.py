    if n == 1:
        return [1]

    result = []
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        result.append(n)

    return sorted([x for x in result if x % 2 != 0])

