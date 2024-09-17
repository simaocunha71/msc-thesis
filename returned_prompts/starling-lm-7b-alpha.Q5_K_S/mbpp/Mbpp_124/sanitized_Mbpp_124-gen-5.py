import cmath
from math import isclose
def angle_complex(a, b):
    return cmath.phase(a + b * 1j)