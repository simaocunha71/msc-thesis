def convert(n):
    r = abs(n)
    phi = cmath.phase(n)
    return (r, phi)