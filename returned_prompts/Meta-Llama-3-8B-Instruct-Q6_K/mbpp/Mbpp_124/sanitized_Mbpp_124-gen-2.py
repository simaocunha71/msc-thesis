import math
def angle_complex(real, imag):
    return math.atan2(imag, real)  # return the angle in radians
    # return math.degrees(math.atan2(imag, real))  # return the angle in degrees
    # return math.degrees(math.atan2(imag, real))  # return the angle in degrees with rounding to 2 decimal places
    # return round(math.degrees(math.atan2(imag, real)),2)  # return the angle in degrees with rounding to 2 decimal places