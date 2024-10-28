def convert(c):
    r = c.real**2 + c.imag**2
    theta = math.atan2(c.imag, c.real)
    return (r, theta)  # or return (math.sqrt(r), theta) for magnitude and angle in radians