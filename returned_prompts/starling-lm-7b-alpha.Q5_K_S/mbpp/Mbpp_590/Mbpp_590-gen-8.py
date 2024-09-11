"""
from math import pi, cos, sin

def polar_rect(r, theta):
    x = r * cos(theta)
    y = r * sin(theta)
    return (x, y)

def test_polar_rect():
    import unittest

    class TestPolar(unittest.TestCase):
        def test_polar_rect(self):
            self.assertEqual(polar_rect(3, 4 * pi / 4), (5.0, 0.9272952180016122), 'Wrong rectangular coordinates')

        def test_polar_rect(self):
            self.assertEqual(polar_rect(3, 4 * pi / 4), (5.0, 0.9272952180016122), 'Wrong rectangular coordinates')

    test_polar_rect()


test_polar_rect()
"""

"""
In Python, the complex number is represented as a + bi where a is the real part and b is the imaginary part.
"""

from math import pi, cos, sin

def polar_rect(r, theta):
    x = r * cos(theta)
    y = r * sin(theta)
    return (x + y * 1j, x - y * 1j)

def test_polar_rect():
    import unittest

    class TestPolar(unittest.TestCase):
        def test_polar_rect(self):
            self.assertEqual(polar_rect(3, 4 * pi / 4), (5.0 + 0.9272952180016122j, 5.0 - 0.9272952180016122j), 'Wrong rectangular coordinates')

        def test_polar_rect(self):
            self.assertEqual(polar_rect(3, 4 * pi / 4), (5.0 + 0.9272952180016122j, 5.0 - 0.