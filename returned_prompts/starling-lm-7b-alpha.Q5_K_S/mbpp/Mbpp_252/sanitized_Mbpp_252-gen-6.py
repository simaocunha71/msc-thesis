def convert(z):
    r = z.real
    theta = np.arctan2(z.imag, z.real)
    return r, theta