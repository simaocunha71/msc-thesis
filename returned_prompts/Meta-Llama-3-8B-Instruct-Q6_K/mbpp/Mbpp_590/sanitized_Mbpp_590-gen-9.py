import cmath
def polar_rect(r,theta):
    x = r * cmath.cos(theta)
    y = r * cmath.sin(theta)
    return (x.real, x.imag) if x.imag != 0 else (x.real, 0) if x.real >= 0 else (x.real, 0) if x.imag < 0 else (0, 0) if x.real < 0 else (x.real, x.imag)