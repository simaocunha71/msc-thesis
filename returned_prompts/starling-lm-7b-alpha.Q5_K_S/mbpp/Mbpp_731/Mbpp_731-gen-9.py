"""
import math

def lateralsurface_cone(r,h):
    # Lateral surface area of a cone is given by pi*r*sqrt(r^2+h^2)
    return math.pi*r*math.sqrt(r**2+h**2)

lateral_surface_area = lateralsurface_cone(5,12)
print(lateral_surface_area)

"""
def lateralSurfaceArea(radius, height):
    return 3.14159 * radius * math.sqrt((radius ** 2 + height ** 2))

def test_lateralSurfaceArea():
    assert lateralSurfaceArea(5, 12) == 204.20352248333654
    print("Test Passed!")

test_lateralSurfaceArea()

"""
def lateralSurfaceArea(radius, height):
    return 3.14159 * radius * math.sqrt((radius ** 2 + height ** 2))

def test_lateralSurfaceArea():
    assert lateralSurfaceArea(5, 12) == 204.20352248333654
    print("Test Passed!")

test_lateralSurfaceArea()
"""


