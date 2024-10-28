    if n > m:
        return -1

    sum = 0
    for i in range(n, m + 1):
        sum += i

    avg = round(sum / (m - n + 1))

    return bin(avg)[2:]