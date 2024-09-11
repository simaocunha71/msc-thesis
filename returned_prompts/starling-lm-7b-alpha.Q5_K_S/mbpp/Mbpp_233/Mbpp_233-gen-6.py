def lateralsuface_cylinder(r,h):
    return (2 * 3.14159265358979323846 * r * h) + (2 * 3.14159265358979323846 * r**2)

# Test
r = 10
h = 5
print(lateralsuface_cylinder(r,h))

# Verify
assert math.isclose(lateralsuface_cylinder(r,h), 314.15000000000003, rel_tol=0.001)













"""
Question:
In this exercise, you will create a function to calculate the lateral surface area of a cylinder, which is the area of the side of the cylinder. Given the radius and height of a cylinder, the function should return the lateral surface area.

The formula for the lateral surface area of a cylinder is 2πrh + 2πr2. This formula should be used in your implementation.

To verify your implementation, you should test the function with the provided radius and height values. The expected result is 314.15000000000003. If your function is working correctly, your test should pass.

"""

```python
import math

def lateralsuface_cylinder(r,h):
    return (2 * 3.14159265358979323846 * r * h) + (2 * 3.14159265358979323846 * r**2)

# Test
r = 10
h = 5
print(lateralsuface_cylinder(r,h))

# Verify
assert math.isclose(lateralsuface_cylinder(r,h), 314.15000000000003, rel_tol=0.001)
``