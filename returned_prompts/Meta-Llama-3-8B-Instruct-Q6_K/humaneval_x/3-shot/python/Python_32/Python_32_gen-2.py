    if len(xs) % 2 != 0:
        raise ValueError("xs must have even number of coefficients")

    if abs(xs[0]) > max(abs(x) for x in xs[1:]):
        return -xs[0] / xs[-1]
    else:
        raise ValueError("xs must have largest non zero coefficient as first one")


