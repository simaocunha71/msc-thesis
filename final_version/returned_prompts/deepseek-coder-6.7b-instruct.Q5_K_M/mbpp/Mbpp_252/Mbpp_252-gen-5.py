"""
import math

def convert(comp_num):
    magnitude = abs(comp_num)
    angle = math.atan2(comp_num.imag, comp_num.real)
    return (magnitude, angle)

print(convert(1))  # (1.0, 0.0)
"""

