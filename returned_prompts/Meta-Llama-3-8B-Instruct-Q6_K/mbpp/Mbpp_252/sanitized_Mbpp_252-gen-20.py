def convert(z):
    r = (z.real**2 + z.imag**2)**0.5
    theta = 0 if z.real >= 0 else math.pi
    theta += math.atan2(z.imag, z.real)
    return r, theta