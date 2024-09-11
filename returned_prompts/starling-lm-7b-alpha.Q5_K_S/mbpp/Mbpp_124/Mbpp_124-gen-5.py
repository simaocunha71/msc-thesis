"""
import cmath
from math import isclose

def angle_complex(a, b):
    return cmath.phase(a + b * 1j)
"""

import cmath
from math import isclose

def angle_complex(a, b):
    return cmath.phase(a + b * 1j)

# assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)

