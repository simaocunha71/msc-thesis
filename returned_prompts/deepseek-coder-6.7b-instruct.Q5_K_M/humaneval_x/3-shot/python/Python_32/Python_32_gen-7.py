    def newton_raphson(xs, x):
        """
        Implements Newton Raphson method for root finding.
        """
        while abs(poly(xs, x)) > 1e-6:
            x = x - poly(xs, x) / poly(poly_diff(xs), x)
        return x

    return newton_raphson(xs, 0)


