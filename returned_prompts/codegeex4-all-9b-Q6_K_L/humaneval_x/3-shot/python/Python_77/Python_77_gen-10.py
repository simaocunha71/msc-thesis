    def is_cube(n):
        if n == 0:
            return True
        if n < 0:
            n = -n
        return round(n ** (1/3)) ** 3 == n

    return is_cube(a)