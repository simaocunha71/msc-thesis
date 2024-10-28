    n = len(xs) - 1
    m = n // 2
    while m > 0:
        if xs[m] != 0:
            break
        m -= 1

    if m == 0:
        return None

    a = xs[m]
    b = xs[n - m]

    if b == 0:
        return None

    x = -a / b

    if poly([0, x], x) == 0:
        return x

    return None
