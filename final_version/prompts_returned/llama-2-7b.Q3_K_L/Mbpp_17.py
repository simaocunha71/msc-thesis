"""
Write a function that returns the perimeter of a square given its side length as input.
assert square_perimeter(10)==40
"""

def square_perimeter(side):
    return 2*((side[0]+side[1])+ side[2] + (side[3]+side[4]))