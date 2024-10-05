    if len(xs) % 2 == 1:
        xs.pop()

    n = int(len(xs) / 2)
    a, b = 0, 0
    for i in range(n):
        a += xs[2 * i] * xs[2 * i + 1]
        b += xs[2 * i + 1] ** 2

    return -a / b
