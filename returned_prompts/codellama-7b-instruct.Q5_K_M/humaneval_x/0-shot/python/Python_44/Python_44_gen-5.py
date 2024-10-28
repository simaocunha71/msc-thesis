
    base_repr = ''
    while x > 0:
        base_repr = str(x % base) + base_repr
        x //= base
    return base_repr