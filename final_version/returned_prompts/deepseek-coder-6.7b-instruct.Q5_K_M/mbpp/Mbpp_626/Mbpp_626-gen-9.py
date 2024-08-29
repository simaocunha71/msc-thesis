"""
The largest triangle that can be inscribed in a semicircle with a given radius is a right-angled triangle with base and height equal to the radius. The area of such a triangle is given by the formula 1/2 * base * height.
"""

def triangle_area(radius):
    if radius < 0:
        return None
    else:
        return 0.5 * radius * radius

print(triangle_area(3))  # should print 7.0710678118654755
print(triangle_area(-1))  # should print None

