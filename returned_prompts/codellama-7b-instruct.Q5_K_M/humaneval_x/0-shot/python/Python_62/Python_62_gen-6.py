
def derivative(xs):
    return xs[:-1] + [2*x for x in xs[:-1]]
