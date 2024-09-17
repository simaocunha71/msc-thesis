import cmath
def angle_complex(real: int, imag: int):
    return cmath.phase(complex(real, imag))