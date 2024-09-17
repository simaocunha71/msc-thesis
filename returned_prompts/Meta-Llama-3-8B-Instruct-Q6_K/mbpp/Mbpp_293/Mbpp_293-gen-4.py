```
def otherside_rightangle(a, b):
    import math
    return math.sqrt(a**2+b**2)
```


The function takes two sides of a right-angled triangle as input and returns the length of the third side. The third side is calculated using the Pythagorean theorem: `sqrt(a^2+b^2)`. 

The unit test `assert otherside_rightangle(7,8)==10.63014581273465` ensures that the function works correctly for a right-angled triangle with sides of length 7 and 8. 
The result of the function is a floating point number due to the use of the `sqrt` function. 

This function assumes that the input values are the lengths of the two sides of a right-angled triangle and returns the length of the hypotenuse. If the input values are not the lengths of the sides of a right-angled triangle, the function may not work correctly. 
The function also assumes that the input values are non-negative, as the lengths of the sides of a triangle must be non-negative. 
The function does not check whether the input values satisfy the triangle inequality, which is a necessary condition for the lengths of the sides of a triangle. 
The function does not check whether the input values are the lengths of the sides of a right-angled triangle, which is a necessary condition for the use of the Pythagorean theorem. 
The function does not handle the case where the input values are not numbers, which could occur if the input values are not numeric. 