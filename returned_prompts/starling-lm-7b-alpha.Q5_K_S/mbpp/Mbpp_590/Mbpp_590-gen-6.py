"""
To convert polar coordinates to rectangular coordinates, we can use the following formulas:

x = r * cos(θ)
y = r * sin(θ)

Here, r is the magnitude of the polar coordinate and θ is the angle that the line makes with the positive x-axis.

We can write a function in Python to perform this conversion:

def polar_rect(r, theta):
    import math
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x,y)
"""
import math
def polar_rect(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x,y)

# Test the function
assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947