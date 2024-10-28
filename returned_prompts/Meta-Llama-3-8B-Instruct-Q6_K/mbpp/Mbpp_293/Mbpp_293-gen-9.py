```
import math

def otherside_rightangle(a, b):
    return math.sqrt(a**2+b**2)
```


The problem is asking to write a function that finds the length of the third side of a right-angled triangle, given the lengths of the other two sides. 

The unit test `assert otherside_rightangle(7,8)==10.63014581273465` suggests that the function should return the length of the hypotenuse (the side opposite the right angle) of the right-angled triangle. 

To solve this, we can use the Pythagorean theorem, which states that the square of the length of the hypotenuse is equal to the sum of the squares of the lengths of the other two sides. 

Here is the Python function that implements this:

```python
import math

def otherside_rightangle(a, b):
    return math.sqrt(a**2+b**2)
```

This function takes two arguments, `a` and `b`, which are the lengths of the two sides of the right-angled triangle. It returns the length of the hypotenuse, which is calculated using the Pythagorean theorem. The `math.sqrt` function is used to calculate the square root of the sum of the squares of `a` and `b`. 

The unit test `assert otherside_rightangle(7,8)==10.63014581273465` passes with this function, indicating that it correctly calculates the length of the hypotenuse of a right-angled triangle given the lengths of the other two sides. 