def is_polite(n):
    polite_sum = 0
    i = 1
    while polite_sum < n:
        i += 1
        polite_sum += i
        polite_sum += i - 1
    return polite_sum