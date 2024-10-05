    if len(xs) % 2 != 0:
        raise ValueError("List of coefficients should have even length")

    if xs[0] == 0:
        raise ValueError("Largest coefficient should be non-zero")

    x = 1

    while poly([xs[0]] + xs[2:], x) != 0:
        x += 1e-5

    return x


