The problem is asking for a function that finds the length of the third side of a right-angled triangle given the lengths of the other two sides. This is a classic problem in geometry, and the solution involves using the Pythagorean theorem.

However, the problem statement is a bit unclear, as it doesn't specify whether the given sides are the length of the hypotenuse and one of the legs or the lengths of two legs. But, thanks to the unit test provided, we can infer that the function should take the lengths of the two legs as input and return the length of the hypotenuse.

Here is the solution:
```
import math

def otherside_rightangle(a, b):
    return math.sqrt(a**2 + b**2)
```
This function uses the Pythagorean theorem to calculate the length of the hypotenuse (the third side of the right-angled triangle) given the lengths of the two legs (a and b). The `math.sqrt` function is used to calculate the square root of the sum of the squares of a and b. This is the length of the hypotenuse.