def convert(c):
    r = abs(c)
    theta = 0 if c.real >= 0 else 180 if c.real < 0 else 90
    if c.imag > 0:
        theta += 90
    return (r, theta)  # radius and angle in degrees