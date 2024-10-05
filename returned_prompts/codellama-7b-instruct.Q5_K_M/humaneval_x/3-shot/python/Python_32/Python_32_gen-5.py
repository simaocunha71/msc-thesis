    n = len(xs) - 1
    zero = 0
    for i in range(n):
        zero += xs[i] * math.pow(x, n - i)

    return zero


