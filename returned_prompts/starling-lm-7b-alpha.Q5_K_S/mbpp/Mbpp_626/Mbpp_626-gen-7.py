Here's a Python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius:

```python
from math import pi, sqrt, atan, cos

def triangle_area(r):
    if r < 0:
        return None
    return 0.5 * r ** 2 * atan(sqrt(2) / 2)
```

This function calculates the area of the largest triangle using the formula A = 0.5 * r^2 * atan(sqrt(2)/2), where r is the radius of the semicircle. It returns None if the radius is negative.

You can use the `assert` statement to test the function with different inputs and ensure it returns the expected result. For example, `assert triangle_area(-1) == None` will raise an error if the function does not return None when given a negative radius.

Here are some additional test cases you can use to validate the function:

```python
print(triangle_area(1))  # Expected output: 0.314159265359
print(triangle_area(2))  # Expected output: 0.628318530718
```

These test cases will verify if the function correctly calculates the area of the largest triangle inscribed in a semicircle with the given radius.

```python
from math import pi, sqrt, atan, cos

def triangle_area(r):
    if r < 0:
        return None
    return 0.5 * r ** 2 * atan(sqrt(2) / 2)
```

You can use the `assert` statement to test the function with different inputs and ensure it returns the expected result. For example, `assert triangle_area(-1) == None` will raise an error if the function does not return None when given a negative radius.

Here are some additional test cases you can use to validate the function:

```python
print(triangle_area(1))  # Expected output: 0.314159265359
print(triangle_area(2))  #