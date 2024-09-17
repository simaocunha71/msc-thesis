def is_polite(n):
    def nth_polite(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    return nth_polite(n) + n