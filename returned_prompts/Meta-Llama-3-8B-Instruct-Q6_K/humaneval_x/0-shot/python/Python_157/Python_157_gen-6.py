    # This function uses the Pythagorean theorem to check if the sides form a right-angled triangle.
    # The theorem states that for a right-angled triangle, the square of the hypotenuse (c) is equal to the sum of the squares of the other two sides (a and b).
    # So, if a^2 + b^2 = c^2, then the triangle is a right-angled triangle.

    # First, we sort the sides in ascending order to ensure that a is the smallest and c is the largest.
    sides = sorted([a, b, c])

    # Then we check if the square of the hypotenuse is equal to the sum of the squares of the other two sides.
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

B:

def right_angle_triangle(a, b, c):
    # We can also use the condition that for a right-angled triangle, the square of the hypotenuse (c) is equal to the sum of the squares of the other two sides (a and b).
    # So, if a^2 + b^2 = c^2, then the triangle is a right-angled triangle.

    # First, we sort the sides in ascending order to ensure that a is the smallest and c is the largest.
    sides = sorted([a, b, c])

    # Then we check if the square of the hypotenuse is equal to the sum of the squares of the other two sides.
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

C:

def right_angle_triangle(a, b, c):
    # We can also use the condition that for a right-angled triangle, one side must be the hypotenuse (which is the longest side) and the other two sides must be the legs (which are the shorter sides).
    # So, if the longest side is the hypotenuse, then the triangle is a right-angled triangle.

    # First, we sort the sides in ascending order to ensure that a is the smallest and c is the largest.
    sides = sorted([a, b, c])

    # Then we check if the longest side is the hypotenuse.
    if c**2 == a**2 + b**2:
        return True
    else:
        return False

D