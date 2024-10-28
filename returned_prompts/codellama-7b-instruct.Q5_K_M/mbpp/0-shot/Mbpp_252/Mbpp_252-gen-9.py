def convert(z):
    return (z.real**2 + z.imag**2)**0.5, atan2(z.imag, z.real)
