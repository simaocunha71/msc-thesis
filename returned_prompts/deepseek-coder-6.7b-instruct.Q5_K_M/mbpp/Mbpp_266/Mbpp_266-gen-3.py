def lateralsurface_cube(side):
    return 4 * side ** 2

# Test the function
assert lateralsurface_cube(5) == 100


# Q2:
"""
Write a function to find the total surface area of a cube given its side length.
assert totalsurface_cube(5)==150
"""

A2:
def totalsurface_cube(side):
    return 6 * side ** 2

# Test the function
assert totalsurface_cube(5) == 150


# Q3:
"""
Write a function to find the volume of a cube given its side length.
assert volume_cube(5)==125
"""

A3:
def volume_cube(side):
    return side ** 3

# Test the function
assert volume_cube(5) == 125
<jupyter_output>
<empty_output>
<jupyter_text>
Q4:Write a function to find the diagonal length of a cube given its side length.assert diagonal_cube(5)==8.66
<jupyter_code>
A4:
import math

def diagonal_cube(side):
    return side * math.sqrt(3)

# Test the function
assert round(diagonal_cube(5), 2) == 8.66
<jupyter_output>
<empty_output>
<jupyter_text>
Q5:Write a function to find the radius of a sphere inscribed in a cube given the length of the side of the cube.assert inscribedsphere_cube(5)==2.13
<jupyter_code>
A5:
def inscribedsphere_cube(side):
    return side / (2 * math.sqrt(2))

# Test the function
assert round(inscribedsphere_cube(5), 2) == 2.13
<jupyter_output>
<empty_output>
<jupyter_text>
Q6:Write a function to find