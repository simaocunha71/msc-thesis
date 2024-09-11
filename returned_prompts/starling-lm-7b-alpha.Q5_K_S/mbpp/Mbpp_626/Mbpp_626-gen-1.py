To find the area of the largest triangle that can be inscribed in a semicircle with a given radius, we can use the following steps:

1. Import the math library to use the pi constant and the square root function.
2. Define a function called triangle_area that takes the radius of the semicircle as an argument.
3. Inside the function, calculate the area of the semicircle using the formula (1/2) * pi * r^2. Store the result in a variable called semicircle_area.
4. Use the formula for the area of a triangle, which is (1/2) * base * height, to calculate the area of the largest triangle that can be inscribed in the semicircle. In this case, the base of the triangle is equal to the radius of the semicircle, and the height is equal to the radius times the square root of 3. Store the result in a variable called triangle_area.
5. Return the calculated triangle_area.

Here's the code for the function:

```python
import math

def triangle_area(r):
    # Calculate the area of the semicircle
    semicircle_area = (1/2) * math.pi * r**2
    # Calculate the area of the largest triangle that can be inscribed in the semicircle
    triangle_area = (1/2) * r * r * math.sqrt(3)
    return triangle_area
```

To test the function, you can use the assert statement to check if the function returns the expected value when the radius is negative. In this case, the function should return None, as it's not possible to have a negative radius for a circle or semicircle. Here's an example of how to test the function:

```python
assert triangle_area(-1) == None
```

This assert statement will raise an AssertionError if the function does not return None when given a negative radius.

```

```

```python

```python

```python

```python

```python

```python

```python

```python
```

```

```

``