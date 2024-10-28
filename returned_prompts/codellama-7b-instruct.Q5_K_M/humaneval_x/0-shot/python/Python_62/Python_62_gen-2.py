

def derivative(xs: list):
    return xs[1:] + [2 * xs[-1] * xs[-2]]
