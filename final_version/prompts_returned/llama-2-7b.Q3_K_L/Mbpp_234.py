"""
Write a function to find the volume of a cube given its side length.
assert volume_cube(3)==27
"""
import math

def volume_cube(length):
    return round(math.pi * length**3, 10)