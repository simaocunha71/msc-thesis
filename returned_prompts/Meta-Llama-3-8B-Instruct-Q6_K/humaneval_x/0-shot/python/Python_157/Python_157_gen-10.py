```
def right_angle_triangle(a, b, c):
    sides = sorted([a, b, c])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    return False
```

The function `right_angle_triangle(a, b, c)` takes three arguments, the lengths of the three sides of a triangle. It first sorts the sides in ascending order using the `sorted()` function. Then, it checks if the sum of the squares of the two shorter sides is equal to the square of the longest side. If it is, the function returns `True`, indicating that the sides form a right-angled triangle. Otherwise, it returns `False`. This is based on the Pythagorean theorem, which states that in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides. In this case, the shortest side is the hypotenuse, and the other two sides are the other two sides of the triangle. If the sum of the squares of these two sides is equal to the square of the shortest side, then the triangle is a right-angled triangle. Otherwise, it is not. This is a simple and efficient way to check if a triangle is right-angled given its side lengths.