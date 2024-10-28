    if n > m:
        return -1
    sum = 0
    for i in range(n, m+1):
        sum += i
    avg = round(sum / (m - n + 1))
    bin_avg = bin(avg)[2:]
    return "0b" + bin_avg.zfill(8)  # Fill with leading zeros if necessary.