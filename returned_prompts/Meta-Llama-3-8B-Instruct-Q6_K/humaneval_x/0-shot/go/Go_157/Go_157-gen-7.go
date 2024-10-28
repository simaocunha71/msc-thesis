The problem is asking you to write a function that determines whether three given sides of a triangle form a right-angled triangle or not. A right-angled triangle is a triangle in which one angle is 90 degrees.

Here is a Python solution for this problem:

```Python
def RightAngleTriangle(a, b, c):
    # check if the sides can form a triangle
    if a + b > c and a + c > b and b + c > a:
        # check if the square of the hypotenuse is equal to the sum of the squares of the other two sides
        if a**2 + b**2 == c**2:
            return True
    return False
```

In this solution, we first check if the three sides can form a triangle by applying the triangle inequality theorem. Then, we check if the square of the hypotenuse (the longest side) is equal to the sum of the squares of the other two sides. If both conditions are met, then the three sides form a right-angled triangle, and we return True. Otherwise, we return False. 

For example, if we call `RightAngleTriangle(3, 4, 5)`, the function will return True because the three sides form a right-angled triangle (a Pythagorean triple). If we call `RightAngleTriangle(1, 2, 3)`, the function will return False because the three sides do not form a right-angled triangle. 