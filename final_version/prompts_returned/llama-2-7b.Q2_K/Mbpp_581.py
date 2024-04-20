"""
Write a python function to find the surface area of a square pyramid with a given base edge and height.
assert surface_Area(3,4) == 33
"""

def surface_Area(base,height):
    surface_area=0
    for i in range(1 ,base+1):   # Base edge
        height=i-1
        area=(height*(i/2))**2
        surface_area+=str(round(area))+'m'

    return surface_Area

print("surface Area of square pyramid",surface_Area(4,3),"m")