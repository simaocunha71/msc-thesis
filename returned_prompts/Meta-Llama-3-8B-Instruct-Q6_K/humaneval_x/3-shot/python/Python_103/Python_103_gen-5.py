    if n > m:
        return -1

    avg = sum(range(n, m+1)) / len(range(n, m+1))
    avg = round(avg)
    return bin(avg)[2:]


