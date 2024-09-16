
def is_nonagonal(n):
    return n == sum(sorted(map(lambda x: pow(x, 3), range(1, n + 1)))[:n])

is_nonagonal(10)

