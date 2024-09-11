"""
Here's a function to find the lateral surface area of a cylinder:

```python
import math

def lateralsuface_cylinder(r, h):
    """
    Calculates the lateral surface area of a cylinder.

    Args:
        r (float): The radius of the cylinder.
        h (float): The height of the cylinder.

    Returns:
        float: The lateral surface area of the cylinder.
    """
    return 2 * math.pi * r * h
```

To use the function and verify its correctness, you can use the `math.isclose()` function to compare the result with the expected value, setting a relative tolerance of 0.001:

```python
assert math.isclose(lateralsuface_cylinder(10, 5), 314.15000000000003, rel_tol=0.001)
```
"""

def lateralsuface_cylinder(r, h):
    """
    Calculates the lateral surface area of a cylinder.

    Args:
        r (float): The radius of the cylinder.
        h (float): The height of the cylinder.

    Returns:
        float: The lateral surface area of the cylinder.
    """
    return 2 * math.pi * r * h

# Testing the function
r = 10
h = 5
expected_result = 314.15000000000003

result = lateralsuface_cylinder(r, h)

# Comparing the result with the expected value using math.isclose()
assert math.isclose(result, expected_result, rel_tol=0.001)

print("The lateral surface area of the cylinder is:", result)

```
This code defines the `lateralsuface_cylinder()` function to calculate the lateral surface area of a cylinder. It then tests the function by providing sample values for the radius (`r`) and height (`h`) of the