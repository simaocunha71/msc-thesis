    import math

    def is_cube(n):
        if n < 0:
            n = -n
        root = round(n ** (1. / 3.))
        return n == root ** 3

    return is_cube(a)

