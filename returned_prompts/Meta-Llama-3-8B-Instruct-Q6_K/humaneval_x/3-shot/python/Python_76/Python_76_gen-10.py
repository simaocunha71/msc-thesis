    import math

    def is_simple_power(x, n):
        root = math.pow(x, 1.0 / n)
        return int(root + 0.5) == root


