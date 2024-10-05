    coeff = xs[::-1]
    x = 0
    for c in coeff:
        x -= c / (x if c != 0 else 1)
    return x


