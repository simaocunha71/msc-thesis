    n = len(xs) // 2
    while xs[n] == 0:
        n -= 1

    while xs[n + 1] == 0:
        n += 1

    x = -xs[n] / xs[n + 1]
    return x
