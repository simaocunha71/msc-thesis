"""
import math

def angle_complex(z):
    return math.atan2(z.imag, z.real)

print(math.isclose(angle_complex(0+1j), 1.5707963267948966, rel_tol=0.001))
"""

