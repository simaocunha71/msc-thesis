```
import math

def lateralsuface_cylinder(radius, height):
    return 2 * math.pi * radius * (radius + height)
```


This function calculates the lateral surface area of a cylinder by using the formula: 2 * π * r * (r + h), where r is the radius and h is the height of the cylinder.

The unit test `assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)` ensures that the function is working correctly for a given input. The `math.isclose` function is used to compare the result of the function with the expected result, allowing for a small tolerance due to floating point precision issues.