import unittest
def parabola_directrix(a, b, c):
    """Find the directrix of a parabola."""
    d = -b / 2 / a
    e = d * d * a
    return e