import math
def angle_complex(real: complex, imag: complex) -> float:
    return math.atan2(imag.real, real.real)  # math.atan2 is used to get the correct quadrant