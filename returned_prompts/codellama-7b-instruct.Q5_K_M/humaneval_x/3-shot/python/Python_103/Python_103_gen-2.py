    if n > m:
        return -1
    else:
        sum = 0
        for i in range(n, m + 1):
            sum += i
        average = sum / (m - n + 1)
        return bin(round(average))


