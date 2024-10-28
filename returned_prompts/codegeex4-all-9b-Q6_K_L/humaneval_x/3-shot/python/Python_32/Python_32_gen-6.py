    n = len(xs) - 1
    while xs[n] == 0:
        n -= 1

    a = xs[n]
    b = xs[n - 1] if n > 0 else 0
    c = xs[n - 2] if n > 1 else 0
    d = xs[n - 3] if n > 2 else 0

    p = b / a
    q = c / a
    r = d / a
    s = (-p + math.sqrt(p ** 2 - 4 * q)) / 2

    return (-p + s - r) / q


