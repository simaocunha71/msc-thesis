def is_polite(n):
    polite_count = 0
    i = 0
    while polite_count < n:
        i += 1
        if all(i - j > 0 for j in range(1, i)):
            polite_count += 1
    return i - 1