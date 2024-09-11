"""
To find the volume of a sphere, the formula is:
V = (4/3) * pi * r^3

Here's a function that implements this formula:

```python
import math

def volume_sphere(r):
    """Calculate the volume of a sphere given the radius r."""
    return (4/3) * math.pi * r**3
```

To test this function, we can use the `math.isclose()` function to check if the calculated volume of a sphere with radius 10 is approximately equal to 4188.790204786391, with a relative tolerance of 0.001. Here's how we can do that:

```python
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
```

This assertion will pass if the calculated volume is within a relative tolerance of 0.001 of the expected volume. If the assertion fails, an `AssertionError` will be raised.

By using this function and the assertion, you can ensure that your implementation of the volume of a sphere is accurate within a specified tolerance.

"""
import math

def volume_sphere(r):
    """Calculate the volume of a sphere given the radius r."""
    return (4/3) * math.pi * r**3

assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)




























































































































