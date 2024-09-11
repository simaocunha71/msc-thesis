Here is a Python function that solves the problem:

```python
import math

def triangle_area(r):
    if r < 0:
        return None
    elif r == 0:
        return 0
    else:
        return (math.pi * r**2) / 4
```

In this code, we start by checking if the radius `r` is negative. If it is, we return None to indicate that the area cannot be calculated with a negative radius. If the radius is zero, we return 0 because a circle with zero radius has no area. Otherwise, we use the formula for the area of a triangle inscribed in a semicircle, which is (pi * r^2) / 4, and return the result.

To use this function, you can call it with a radius value and print the result:

```python
r = 5
print(triangle_area(r))
```

This will print the area of the largest triangle that can be inscribed in a semicircle with a radius of 5.

```python
import math

def triangle_area(r):
    if r < 0:
        return None
    elif r == 0:
        return 0
    else:
        return (math.pi * r**2) / 4
```

To test the function with a negative radius value, you can call it with -1 and check the result:

```python
print(triangle_area(-1))
```

This will print None, as the function returns None for negative radius values.

To test the function with a radius value of 0, you can call it with 0 and check the result:

```python
print(triangle_area(0))
```

This will print 0, as the function returns 0 for radius values of 0.

To test the function with a positive radius value, you can call it with a positive integer value and check the result:

```python
print(triangle_area(5))
```

This will print the area of the largest triangle that can be inscribed in a semicircle with a radius of 5, which is approximately 6.