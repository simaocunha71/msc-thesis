Here's a Python function that calculates the area of the largest triangle that can be inscribed in a semicircle with a given radius:

```python
import math

def triangle_area(radius):
    # Check if the radius is valid
    if radius <= 0:
        return None
    # Calculate the area of the semicircle
    area_semicircle = math.pi * radius ** 2 / 2
    # Calculate the area of the triangle by subtracting the area of the semicircle from the area of the circle
    area_triangle = area_semicircle * 2 / math.pi
    return area_triangle
```

You can use the `assert` statement to verify the correctness of the function. Here's an example:

```python
assert triangle_area(-1) == None
```

This `assert` statement checks if the `triangle_area` function returns `None` when given a radius of `-1`. The `==` operator compares the two values, and if they are not equal, an `AssertionError` is raised.

The `triangle_area` function first checks if the radius is valid (i.e., greater than zero). If the radius is not valid, it returns `None`. Otherwise, it calculates the area of the semicircle using the formula `math.pi * radius ** 2 / 2` and the area of the triangle by subtracting the area of the semicircle from the area of the circle using the formula `area_semicircle * 2 / math.pi`. Finally, it returns the calculated area of the triangle.

By using the `assert` statement, you can ensure that the `triangle_area` function behaves correctly and returns `None` when given an invalid radius.

```python
def triangle_area(radius):
    # Check if the radius is valid
    if radius <= 0:
        return None
    # Calculate the area of the semicircle
    area_semicircle = math.pi * radius ** 2 / 2
    # Calculate the area of the triangle by subtracting the area of the semicircle from the area of the circle
