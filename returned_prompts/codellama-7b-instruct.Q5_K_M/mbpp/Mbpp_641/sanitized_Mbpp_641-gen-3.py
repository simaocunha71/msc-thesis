def is_nonagonal(n):
    return n == sum(x**2 for x in range(1, int(n**0.5) + 1))