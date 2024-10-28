def is_polite(n):
    def polite_no(a, b):
        return (a + b) + (a + b + 1)
    count = 0
    i = 1
    j = 1
    while True:
        if count == n:
            return polite_no(i, j)
        count += 1
        i += 1
        j += 1