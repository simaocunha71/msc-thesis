    if n > m:
        return -1
    else:
        total = 0
        for i in range(n, m + 1):
            total += i
        return str(bin(round(total / (m - n + 1))))[2:]
