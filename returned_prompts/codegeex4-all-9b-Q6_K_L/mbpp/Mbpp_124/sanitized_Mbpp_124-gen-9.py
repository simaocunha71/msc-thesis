import math
def angle_complex(real, imag):
    if real == 0 and imag == 0:
        raise ValueError("Cannot compute angle of a complex number with both real and imaginary parts equal to zero")
    return math.atan2(imag, real)