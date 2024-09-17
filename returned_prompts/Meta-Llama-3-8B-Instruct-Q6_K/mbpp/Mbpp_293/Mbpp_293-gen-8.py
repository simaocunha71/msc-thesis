The problem is asking to write a function that takes the lengths of two sides of a right-angled triangle as input and returns the length of the third side. 

The Pythagorean theorem states that the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides. Therefore, the length of the third side can be calculated as the square root of the sum of the squares of the other two sides.

Here is a Python function that implements this:

```
import math

def otherside_rightangle(a, b):
    return math.sqrt(a**2 + b**2)
```

This function takes two arguments, a and b, which are the lengths of the two sides of the right-angled triangle. It returns the length of the hypotenuse (the third side) as the square root of the sum of the squares of a and b. The unit test `assert otherside_rightangle(7,8)==10.63014581273465` ensures that the function works correctly. 

For example, if the two sides of the triangle have lengths 7 and 8, the function will return the length of the hypotenuse as approximately 10.63014581273465, which is the correct value according to the Pythagorean theorem. 