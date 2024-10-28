The problem is asking to write a function that takes the lengths of two sides of a right-angled triangle as input and returns the length of the third side. 

However, the problem doesn't specify the lengths of the two sides. But, based on the unit test provided, `otherside_rightangle(7,8)` should return `10.63014581273465`, we can assume that the function should return the length of the third side of a right-angled triangle with given two sides.

The length of the third side (hypotenuse) can be calculated using the Pythagorean theorem, which is `hypotenuse = sqrt(a^2 + b^2)`, where `a` and `b` are the lengths of the other two sides.

Here is the solution in Python:
```
import math

def otherside_rightangle(a, b):
    return math.sqrt(a**2 + b**2)
```
This function takes two arguments `a` and `b`, which are the lengths of the two sides of the right-angled triangle. It returns the length of the third side (hypotenuse) calculated using the Pythagorean theorem. The `math.sqrt` function is used to calculate the square root. The `**` operator is used to raise the numbers to the power of 2. 

The unit test `assert otherside_rightangle(7,8)==10.63014581273465` is passed by this function. The length of the third side of the right-angled triangle with sides of length 7 and 8 is approximately 10.63014581273465, which is the expected output of the function. 