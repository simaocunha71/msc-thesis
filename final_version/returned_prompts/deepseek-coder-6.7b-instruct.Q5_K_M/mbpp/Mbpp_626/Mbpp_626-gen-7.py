
def triangle_area(radius):
    if radius < 0:
        return None
    return 0.5 * radius ** 2

assert triangle_area(-1) == None
assert triangle_area(1) == 0.5
assert triangle_area(2) == 2.0
assert triangle_area(3) == 4.5
"""

