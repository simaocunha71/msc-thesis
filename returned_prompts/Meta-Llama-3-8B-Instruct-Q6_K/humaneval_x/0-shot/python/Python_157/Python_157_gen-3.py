```
def right_angle_triangle(a, b, c):
    # Check if the given sides form a valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return False

    # Check if the sides form a right-angled triangle
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True

    return False
```
In this function, we first check if the given sides form a valid triangle by applying the triangle inequality theorem. If the sides do not form a valid triangle, we return False.

Then, we check if the sides form a right-angled triangle by applying the Pythagorean theorem. If the sum of the squares of the two smaller sides is equal to the square of the largest side, then the triangle is a right-angled triangle.

Finally, if the sides do not form a right-angled triangle, we return False. If the sides form a right-angled triangle, we return True.