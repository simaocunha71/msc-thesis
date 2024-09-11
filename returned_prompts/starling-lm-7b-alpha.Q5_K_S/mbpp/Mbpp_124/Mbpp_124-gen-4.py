"""
import cmath

def angle_complex(a, b):
    return cmath.phase(complex(a,b))

"""
"""

def test_angle_complex():
    assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)

if __name__ == '__main__':
    test_angle_complex()
"""

import math
from functools import reduce

def angle_complex(a, b):
    return reduce(lambda x, y: complex(x, y), [a, b])

"""
"""

def test_angle_complex():
    assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)

if __name__ == '__main__':
    test_angle_complex()

"""

def angle_complex(a, b):
    return math.atan2(b.imag, b.real)

def test_angle_complex():
    assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)

if __name__ == '__main__':
    test_angle_complex()

"""

def angle_complex(a, b):
    return math.atan2(b.imag, b.real)

def test_angle_complex():
    assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)

if __name__ == '__main__':
    test_angle_complex()

"""

def angle_complex(a,