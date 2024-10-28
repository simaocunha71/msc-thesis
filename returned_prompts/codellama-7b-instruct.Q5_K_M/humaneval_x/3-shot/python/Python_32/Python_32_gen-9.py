    n = len(xs) // 2
    x_guess = -xs[n] / xs[n + 1]
    while True:
        x = x_guess
        x_guess = x - poly(xs[n:], x) / poly(xs[:n], x)
        if abs(x_guess - x) < 1e-6:
            return x_guess
