def is_polite(n):
    polite_num = 0
    i = 1
    while True:
        if polite_num + i < n:
            polite_num += i
            i += 1
        else:
            return polite_num + i - 1