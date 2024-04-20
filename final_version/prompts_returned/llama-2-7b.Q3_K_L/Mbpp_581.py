"""
Write a python function to find the surface area of a square pyramid with a given base edge and height.
assert surface_Area(3,4) == 33
"""
class Solution:
    def surfaceArea(self, base: int, height: int):
        return int((base * (1 + 4/3)**height))
