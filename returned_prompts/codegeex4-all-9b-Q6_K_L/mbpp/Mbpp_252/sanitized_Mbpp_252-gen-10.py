import cmath
def convert(n):
    if isinstance(n, complex):
        r, phi = cmath.polar(n)
        return (r, phi)
    else:
        return (n, 0.0)