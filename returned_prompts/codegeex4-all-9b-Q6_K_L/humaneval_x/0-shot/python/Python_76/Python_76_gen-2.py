def is_simple_power(x, n):
    if x == 1:
        return True
    if x % n != 0:
        return False
    return is_simple_power(x / n, n)