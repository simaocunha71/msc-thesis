    def is_power(a, b):
        while a % b == 0:
            a //= b
        return a == 1

    return is_power(x, n) and n > 0 and x > 0

