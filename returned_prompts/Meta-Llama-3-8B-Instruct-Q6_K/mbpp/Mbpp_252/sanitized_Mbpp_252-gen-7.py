def convert(c):
    r = c.real**2 + c.imag**2
    theta = math.atan2(c.imag, c.real)
    return (r**0.5, theta) if r > 0 else (0, 0) if r == 0 else (0, math.pi) if r < 0 else (0, 0) if c.real == 0 else (1, 0) if c.imag == 0 else (1, 0) if c.real == 0 and c.imag > 0 else (1, math.pi/2) if c.real > 0 and c.imag > 0 else (1, 3*math.pi/2) if c.real < 0 and c.imag > 0 else (1, math.pi)
    import math