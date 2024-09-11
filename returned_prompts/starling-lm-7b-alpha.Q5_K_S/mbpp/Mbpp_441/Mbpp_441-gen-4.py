def surfacearea_cube(size):
    return size**2 * 6

# surfacearea_cube(5)

"""
Write a function to calculate the volume of a cube of a given size.
assert vol_cube(5)==125
"""

B:
def vol_cube(size):
    return size**3

# vol_cube(5)

"""
Write a function to calculate the volume of a sphere of a given radius.
assert vol_sphere(5)==523.5987755982989
"""

C:
import math
def vol_sphere(radius):
    return 4 * math.pi * (radius**3) / 3

# vol_sphere(5)

"""
Write a function to calculate the surface area of a sphere of a given radius.
assert surfacearea_sphere(5)==523.5987755982989
"""

D:
import math
def surfacearea_sphere(radius):
    return 4 * math.pi * (radius**2)

# surfacearea_sphere(5)

"""
Write a function to calculate the volume of a cylinder of a given height and radius.
assert vol_cylinder(5, 6)==301.625
"""

E:
import math
def vol_cylinder(height, radius):
    return math.pi * (radius**2) * height

# vol_cylinder(5, 6)

"""
Write a function to calculate the surface area of a cylinder of a given height and radius.
assert surfacearea_cylinder(5, 6)==301.625
"""

F:
import math
def surfacearea_cylinder(height, radius):
    return 2 * math.pi * (radius**2) + 2 * math.pi * radius * height

# surfacearea_cylinder(5, 6)

"""
Write a function to calculate the surface area of a pyramid of a given base area and height.
assert surfacearea_pyramid(