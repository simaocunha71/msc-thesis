"""
The area of the largest triangle inscribed in a semicircle is given by the formula
triangle_area(r) = r * r * pi / 2

Here's a Python function that implements this formula:
"""

def triangle_area(r):
    import math
    if r <= 0:
        return None
    return r * r * math.pi / 2

# Test the function
assert triangle_area(5) == 50 * math.pi / 2
assert triangle_area(-1) == None

"""
The function triangle_area(r) takes a single parameter r, which is the radius of the semicircle. It first checks if the radius is less than or equal to 0, in which case it returns None to indicate an invalid input. Otherwise, it uses the formula triangle_area(r) = r * r * pi / 2 to calculate and return the area of the largest triangle that can be inscribed in the semicircle.

The function uses the math module to access the value of pi.
"""

# Test the function
print(triangle_area(5))  # Should print 50 * pi / 2
print(triangle_area(-1))  # Should print None

```

This Python function calculates the area of the largest triangle that can be inscribed in a semicircle with a given radius, using the formula triangle_area(r) = r * r * pi / 2. It first checks if the radius is less than or equal to 0, in which case it returns None to indicate an invalid input. Otherwise, it uses the formula to calculate and return the area of the largest triangle that can be inscribed in the semicircle. The function uses the math module to access the value of pi.

To test the function, you can call triangle_area(5) to calculate the area of the largest triangle that can be inscribed in a semicircle with a radius of 5, and print the result. Similarly, you can call triangle_area(-1) to calculate the area of the largest triangle that can be inscribed in a semicircle with a radius of -1, and print the result, which should be None.
```
```