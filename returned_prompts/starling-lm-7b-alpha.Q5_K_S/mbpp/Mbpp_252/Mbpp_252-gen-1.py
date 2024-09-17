
def convert(c):
    r = abs(c)
    theta = math.atan(c.imag / c.real)
    if c.real < 0:
        theta += math.pi
    return (r, theta)


