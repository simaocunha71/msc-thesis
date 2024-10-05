    if n > m:
        return -1

    total = 0
    count = 0

    for i in range(n, m+1):
        total += i
        count += 1

    avg = total / count
    rounded_avg = round(avg)
    binary_avg = bin(rounded_avg)[2:]

    return binary_avg

