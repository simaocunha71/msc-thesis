```
import math

def triangle_area(a, b, c):
    if a+b>c and a+c>b and b+c>a:
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        return round(area, 2)
    else:
        return -1
```


Explanation:

This function takes three arguments `a`, `b`, and `c` which are the lengths of the sides of a triangle. It first checks if the three sides form a valid triangle by checking if the sum of any two sides is greater than the third side. If they do, it calculates the area of the triangle using Heron's formula. The area is then rounded to 2 decimal points and returned. If the three sides do not form a valid triangle, the function returns -1. The `math.sqrt` function is used to calculate the square root and the `round` function is used to round the area to 2 decimal points. The `round` function is used with 2 as its second argument to specify the number of decimal points to round to. 

The example `triangle_area(3, 4, 5)` returns 6.00 because the area of the triangle with sides 3, 4, and 5 is 6. The example `triangle_area(1, 2, 10)` returns -1 because the sides 1, 2, and 10 do not form a valid triangle. 

The function `triangle_area` is well-defined because it always returns a value and the value is either the area of the triangle or -1. The function does not modify any external state and it does not have any side effects. It is also deterministic because it always returns the same output for the same input. 

The time complexity of this function is O(1) because it performs a constant number of operations. The space complexity is also O(1) because it uses a constant amount of space to store the variables and the function does not use any data structures that scale with the input size. 

The function can be tested with different inputs to check its correctness. The function should return the correct area for valid triangles and -1 for invalid triangles. 

The function can be used in a program to calculate the area of triangles. It can be used in a loop to calculate the area of multiple triangles. It can also be used in a function that takes a list of triangles and returns a list of their areas.