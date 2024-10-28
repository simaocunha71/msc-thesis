import math
def angle_complex(complex_num):
    return math.atan2(complex_num.imag, complex_num.real)  # Return the angle in radians