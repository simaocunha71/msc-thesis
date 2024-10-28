def is_polite(n):
    def polite_numbers():
        i = 0
        j = 1
        while True:
            i += 1
            j += 1
            yield i + j - 1
    polite = polite_numbers()
    for _ in range(n - 1):
        next(polite)
    return next(polite)  # return the nth polite number