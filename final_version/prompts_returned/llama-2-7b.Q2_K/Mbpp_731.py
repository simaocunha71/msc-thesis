"""
Write a function to find the lateral surface area of a cone given radius r and the height h.
assert lateralsurface_cone(5,12)==204.20352248333654
"""
from math import pi, sin, cos
def lateralsurface_cone (r:float,h:float)->float :
    return 4 * pi * r **2 * h

if __name__ == '__main__':
    print("lateral surface area of cone = %.2f" %(str(lateralsurface_cone(5.0,12))))