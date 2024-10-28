import cmath
def angle_complex(real, imag):
    return cmath.phase(complex(real, imag))
    # return math.atan2(imag, real)  # This will also work, but cmath.phase is more accurate for complex numbers.  # This will also work, but cmath.phase is more accurate for complex numbers.