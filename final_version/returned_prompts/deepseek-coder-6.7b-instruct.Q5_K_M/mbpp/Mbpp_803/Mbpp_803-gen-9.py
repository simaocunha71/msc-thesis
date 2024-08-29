def is_perfect_square(n):
    return n == (int(n ** 0.5)) ** 2

assert not is_perfect_square(10)

