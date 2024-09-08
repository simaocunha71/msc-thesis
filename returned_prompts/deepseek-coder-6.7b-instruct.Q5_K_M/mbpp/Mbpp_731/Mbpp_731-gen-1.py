import math

def lateralsurface_cone(r, h):
    return math.pi * r * math.sqrt(r**2 + h**2)

print(lateralsurface_cone(5,12))

"""
The math.sqrt function is used to calculate the square root and math.pi is a constant representing pi. The formula for the lateral surface area of a cone is given by pi * r * sqrt(r^2 + h^2), where r is the radius and h is the height of the cone.
"""
<jupyter_output>
204.20352248333654
<jupyter_text>
Question 3
<jupyter_code>
