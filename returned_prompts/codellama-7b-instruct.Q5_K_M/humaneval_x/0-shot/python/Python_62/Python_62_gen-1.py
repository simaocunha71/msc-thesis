

def derivative(xs: list):
    return xs[1:] + [2*x*xs[-1] for x in xs[:-1]]
