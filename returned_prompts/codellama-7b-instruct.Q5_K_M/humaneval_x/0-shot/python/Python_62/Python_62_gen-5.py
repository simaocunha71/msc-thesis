
    xs = list(map(lambda x: x, xs))
    xs.reverse()
    dx = [0] * len(xs)
    dx[0] = xs[1]
    for i in range(1, len(xs) - 1):
        dx[i] = xs[i + 1] * (i + 1)
    dx[len(xs) - 1] = xs[len(xs) - 2] * (len(xs) - 1)
    return dx
