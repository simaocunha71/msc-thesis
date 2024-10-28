    if n > m:
        return -1

    sum = 0
    for i in range(n, m + 1):
        sum += i

    avg = sum / (m - n + 1)
    avg = round(avg)
    avg = bin(avg)
    avg = avg[2:]
    return avg


