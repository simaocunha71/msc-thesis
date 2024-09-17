def convert(x):
    r = abs(x)
    theta = math.atan(x.imag / x.real)
    if x.real < 0:
        theta += math.pi
    elif x.imag < 0:
        theta += 2 * math.pi
    return (r, theta)