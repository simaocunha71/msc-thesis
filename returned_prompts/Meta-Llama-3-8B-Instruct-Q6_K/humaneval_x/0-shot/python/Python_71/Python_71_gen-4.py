```
import math

def triangle_area(a, b, c):
    # calculate the semi-perimeter
    s = (a + b + c) / 2
    # check if the sides form a valid triangle
    if s - a > 0 and s - b > 0 and s - c > 0:
        # calculate the area
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        # round the area to 2 decimal points
        return round(area, 2)
    else:
        return -1
```


Testing:

```
print(triangle_area(3, 4, 5))  # Expected output: 6.0
print(triangle_area(1, 2, 10))  # Expected output: -1
```


In this solution, we first calculate the semi-perimeter `s` of the triangle. Then we check if the three sides form a valid triangle by verifying that the sum of any two sides is greater than the third side. If they do, we calculate the area of the triangle using Heron's formula and round it to 2 decimal points. If the sides do not form a valid triangle, we return -1. The `math.sqrt` function is used to calculate the square root of the area. The `round` function is used to round the area to 2 decimal points.