```
def otherside_rightangle(a, b):
    return ((a**2)+(b**2))**0.5
```


The function takes two arguments `a` and `b` which are the lengths of the two sides of a right-angled triangle. It returns the length of the hypotenuse, which is the third side of the triangle. The formula used is the Pythagorean theorem: `hypotenuse = sqrt(a^2 + b^2)`. The unit test `assert otherside_rightangle(7,8)==10.63014581273465` checks if the function returns the correct result for a right-angled triangle with sides of length 7 and 8.