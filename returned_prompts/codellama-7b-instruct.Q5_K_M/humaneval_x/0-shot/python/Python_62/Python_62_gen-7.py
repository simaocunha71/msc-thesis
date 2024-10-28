

def derivative(xs: list):
    return xs[1:] + [0] * (len(xs) - 1)