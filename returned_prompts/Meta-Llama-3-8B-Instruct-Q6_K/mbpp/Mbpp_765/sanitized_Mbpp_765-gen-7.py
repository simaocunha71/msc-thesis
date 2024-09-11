def is_polite(n):
    sum = 0
    k = 1
    while True:
        sum += k
        if sum >= n:
            return sum - n + 1
        k += 1