import cmath
def polar_rect(r, theta):
    x = r * cmath.cos(theta)
    y = r * cmath.sin(theta)
    return (x.real, x.imag) if y.imag == 0 else (x.real, y) if y.real == 0 else (x, y) if x.real == 0 else (x.real, y) if y.imag == 0 else ((x.real, y.imag), y.real + 1j*y.imag)