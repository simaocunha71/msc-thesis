"""
Write a function to find the surface area of a cube of a given size.
assert surfacearea_cube(5)==150
"""
from math import sqrt, pi
def surfacearea_cube(length):
  return (4 * length ** 2 + 6 * (length+1) ** 2 - 3 * (length+1) ** 2) / 6
