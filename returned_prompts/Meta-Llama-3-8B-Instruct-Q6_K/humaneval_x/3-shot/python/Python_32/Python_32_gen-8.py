    if len(xs) % 2 != 0:
        raise ValueError("List of coefficients must have an even number of elements")

    if abs(xs[0]) < abs(xs[1]):
        raise ValueError("Largest non-zero coefficient must be the first one")

    x = -xs[1] / xs[0]
    return round(x, 2) if abs(xs[0]) < 1e-6 else -math.inf


