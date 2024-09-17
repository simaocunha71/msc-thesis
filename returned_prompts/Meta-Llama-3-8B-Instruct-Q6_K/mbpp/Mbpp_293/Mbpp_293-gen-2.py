The problem is asking you to write a function that takes two sides of a right-angled triangle as input and returns the length of the third side. However, the problem does not specify the lengths of the two given sides.

Luckily, the unit test `assert otherside_rightangle(7,8)==10.63014581273465` provides a hint. It suggests that the function should take two sides of the triangle as input and return the length of the third side using the Pythagorean theorem.

Here is the solution:
```python
import math

def otherside_rightangle(a, b):
    return math.sqrt(a**2 + b**2)
```
This function uses the Pythagorean theorem to calculate the length of the third side of the right-angled triangle. The theorem states that the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides. The function returns the square root of the sum of the squares of the input sides. This is the length of the third side of the right-angled triangle.