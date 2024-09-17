import cmath
def convert(c):
    if not isinstance(c, complex):
        raise ValueError("Input must be a complex number")
    if c == 0:
        raise ValueError("Input cannot be zero")
    r = abs(c)
    phi = cmath.phase(c)
    return r, phi