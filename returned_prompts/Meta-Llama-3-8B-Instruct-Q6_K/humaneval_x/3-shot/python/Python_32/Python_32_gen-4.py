    if len(xs) % 2 != 0:
        raise ValueError("List of coefficients must have even number of elements.")

    a = xs[-1]
    b = xs[-2]
    c = xs[-3]

    if a == 0:
        return -b / c
    else:
        raise ValueError("Polynomial has no roots.")


