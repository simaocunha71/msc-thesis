def convert(x):
    if isinstance(x, complex):
        return (x.real, x.imag)
    return (x, 0.0)