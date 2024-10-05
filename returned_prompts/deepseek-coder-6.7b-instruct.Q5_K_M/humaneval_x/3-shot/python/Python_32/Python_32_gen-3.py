    def poly(xs: list, x: float):
        return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

    def deriv(xs: list):
        return [i * coeff for i, coeff in enumerate(xs)][:-1]

    x = 1.0
    while abs(poly(xs, x)) > 1e-6:
        x -= poly(xs, x) / poly(deriv(xs), x)

    return x

