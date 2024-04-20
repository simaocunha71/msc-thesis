"""
Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.
assert triangle_area(-1) == None
"""
import math
def triangle_area(radius):
    if 2*rad >= 3:
        return (rad*(math.pi/2))**2
    elif rad >= 2:
        return (rad*(math.pi/4))**2
    else:
        return None
if __name__ == "__main__":
    triangle_area(1)