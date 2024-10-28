def is_polite(n):
    i = 1
    count = 0
    while count < n:
        if is_polite(i):
            count += 1
        if count == n:
            return i
        i += 1