    n = len(xs) // 2
    if xs[n] == 0:
        raise ValueError("Polynomial has no real root")
    return -xs[n-1] / xs[n] if n > 1 else 0


