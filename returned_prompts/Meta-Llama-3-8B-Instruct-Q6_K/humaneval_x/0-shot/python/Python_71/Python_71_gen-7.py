
Explanation:

This problem is asking to create a function that calculates the area of a triangle given the lengths of its three sides. However, the function should also check if the three sides form a valid triangle. A valid triangle is one where the sum of any two sides is greater than the third side.

The formula to calculate the area of a triangle is given by Heron's formula, which is:

area = sqrt(s * (s - a) * (s - b) * (s - c))

where s is the semi-perimeter of the triangle, which is the sum of the lengths of the three sides divided by 2.

Here is the Python code that solves this problem:

```
import math

def triangle_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return round(area, 2)
    else:
        return -1
```

This function first checks if the three sides form a valid triangle by checking if the sum of any two sides is greater than the third side. If they do form a valid triangle, it calculates the area using Heron's formula and returns it rounded to 2 decimal points. If they do not form a valid triangle, it returns -1.