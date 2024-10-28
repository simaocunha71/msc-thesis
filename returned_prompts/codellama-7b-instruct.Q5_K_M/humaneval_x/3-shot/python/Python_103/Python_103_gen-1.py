    if n > m:
        return -1

    sum = 0
    for i in range(n, m + 1):
        sum += i

    result = sum // (m - n + 1)

    return bin(result)
