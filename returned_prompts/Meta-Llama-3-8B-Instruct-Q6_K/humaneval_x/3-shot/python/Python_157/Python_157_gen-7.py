    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2
    # This function works by sorting the sides of the triangle, then checking
    # if the sum of the squares of the two shorter sides is equal to the square
    # of the longest side. This is the Pythagorean theorem, which is true for
    # right-angled triangles. If this condition is met, the function returns True,
    # otherwise it returns False.