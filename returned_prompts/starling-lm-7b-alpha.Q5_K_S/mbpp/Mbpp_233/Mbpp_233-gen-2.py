To find the lateral surface area of a cylinder, you can use the formula 2πrh, where r is the radius of the base and h is the height of the cylinder. Here's an implementation of the function in Python:

```python
import math

def lateralsuface_cylinder(r,h):
    return 2*math.pi*r*h
```

To test the function, you can use the `math.isclose()` function to compare the result of the function with the expected value of 314.15000000000003 (rounded to the given tolerance) and check if they are equal within the specified relative tolerance. Here's an example of how to test the function:

```python
def test_lateralsuface_cylinder():
    assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
```

You can call the `test_lateralsuface_cylinder()` function to check if the implementation is correct.

Here's the complete code:

```python
import math

def lateralsuface_cylinder(r,h):
    return 2*math.pi*r*h

def test_lateralsuface_cylinder():
    assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.0