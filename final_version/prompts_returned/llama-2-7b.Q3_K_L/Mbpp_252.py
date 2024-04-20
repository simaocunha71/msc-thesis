"""
Write a python function to convert complex numbers to polar coordinates.
assert convert(1) == (1.0, 0.0)
"""
from typing import Tuple

def convert(x: float) -> Tuple[float, float]:
    x = int(x * 256 + .5)
    if x == 256: return -1j, 255
    else: return x / 256.0 - 1j, int((x % 256))
