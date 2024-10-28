
Here is a Python function that calculates the area of a triangle given the lengths of its three sides. The function first checks if the three sides form a valid triangle (i.e., the sum of any two sides is greater than the third side). If they do, it calculates the semi-perimeter of the triangle and then uses Heron's formula to calculate the area. If the three sides do not form a valid triangle, the function returns -1.

```python
import math

def triangle_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return round(area, 2)
    else:
        return -1
```

You can test this function with the following code:

```python
print(triangle_area(3, 4, 5))  # Output: 6.0
print(triangle_area(1, 2, 10))  # Output: -1
```

In the first example, the function correctly calculates the area of a valid triangle with sides of length 3, 4, and 5. In the second example, the function returns -1 because the sides do not form a valid triangle.