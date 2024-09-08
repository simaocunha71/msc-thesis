def is_nonagonal(n):
    def nonagonal(n):
        return (9 * n * (n - 1)) // 2
    i = 1
    while nonagonal(i) < n:
        i += 1
    return i