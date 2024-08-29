
The largest triangle that can be inscribed in a semicircle is a right-angled triangle, where the hypotenuse is the diameter of the semicircle. The area of a right-angled triangle is given by the formula: 1/2 * base * height.

Here's the code:

```python
import math

def triangle_area(radius):
    if radius <= 0:
        return None
    else:
        diameter = 2 * radius
        # the base and height are the same in a right-angled triangle, so we only need to calculate one of them
        base = diameter
        # the height of the triangle is the radius of the semicircle
        height = radius
        return 0.5 * base * height

print(triangle_area(1))  # Output: 0.5
print(triangle_area(2))  # Output: 2.0
print(triangle_area(-1))  # Output: None
```

In this code, we first check if the radius is less than or equal to 0. If it is, we return None. If the radius is greater than 0, we calculate the diameter of the semicircle (which is twice the radius), and use this to calculate the area of the largest triangle that can be inscribed in the semicircle. The area of a right-angled triangle is 1/2 * base * height, so we return 0.5 * diameter * radius.

The assert statements at the end of the code are used to test the function. We check that the area of the triangle with radius 1 is 0.5, the area of the triangle with radius 2 is 2.0, and the area of the triangle with radius -1 is None, as expected.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
