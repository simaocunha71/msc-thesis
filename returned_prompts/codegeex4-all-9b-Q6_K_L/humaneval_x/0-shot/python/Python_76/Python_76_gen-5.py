def is_simple_power(x, n):
    return x == n**int(x/n) if x > 0 else False