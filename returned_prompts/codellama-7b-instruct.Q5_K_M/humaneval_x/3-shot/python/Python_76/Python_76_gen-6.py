    if n == 0 or x == 0:
        return False
    if x == 1:
        return True
    if n == 1:
        return False
    if n == x:
        return True
    if x % n == 0:
        return is_simple_power(x // n, n)
    return False


