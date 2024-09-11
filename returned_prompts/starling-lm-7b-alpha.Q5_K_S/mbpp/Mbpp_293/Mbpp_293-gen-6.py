import math
def otherside_rightangle(base, height):
    h = math.sqrt(base**2 + height**2)
    return h

# Otherside of a right angle triangle is calculated using Pythagorean theorem,
# In this theorem, the square of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the other two sides.
# Here, base and height are considered as the two sides other than the hypotenuse (third side).

"""
As per the problem, the function should return the value of the third side as a float.
We can verify the function by passing the base and height as 7 and 8 respectively.
As per Pythagorean theorem, third side = √(base^2 + height^2) = √(7^2 + 8^2) = 10.63014581273465
Hence, the function should return 10.63014581273465
"""

assert otherside_rightangle(7,8)==10.63014581273465

# The above assert statement will pass if the function correctly calculates the third side of the right angled triangle
```
1
2
3
4
5
6
7
8
```