def parabola_directrix(a,b,c):
    if a == 0:
        raise ValueError("a cannot be 0")
    x = -(b**2)/(4*a) + c
    y = -(b**2)/(4*a)
    directrix = (x, y)
    return directrix