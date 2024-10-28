
def convert(z):
    x, y = z.real, z.imag
    rho = (x**2 + y**2)**0.5
    theta = atan2(y, x)
    return (rho, theta)


