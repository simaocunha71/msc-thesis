
def is_simple_power(x, n):
    if x <= 0 or n <= 0:
        return False
    return x == n ** (x // n)
