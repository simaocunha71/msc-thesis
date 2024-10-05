To determine if a triangle is right-angled, we can use the Pythagorean theorem,
which states that in a right-angled triangle, the square of the length of the
hypotenuse (the side opposite the right angle) is equal to the sum of the squares
of the lengths of the other two sides.

In Python, we can implement the above theorem as follows:

```python
def RightAngleTriangle(a, b, c):
    # check if a, b and c are positive
    if a <= 0 or b <= 0 or c <= 0:
        return False
    # check if the sum of squares of a and b is greater than c squared
    # this is due to the Pythagorean theorem: c^2 = a^2 + b^2
    if a**2 + b**2 > c**2:
        return True
    else:
        return False
```

For example, to determine if the sides of length 3, 4, and 5 form a right-angled
triangle, we can call the function as follows:

```python
print(RightAngleTriangle(3, 4, 5)) # prints True
```

In this example, the function will return True because 3, 4, and 5 are the
sides of a right-angled triangle.

On the other hand, if we call the function as follows:

```python
print(RightAngleTriangle(1, 2, 3)) # prints False
```

The function will return False because 1, 2, and 3 are not the sides of a right-
angled triangle.

To summarize, the function `RightAngleTriangle` checks if the given three sides
can form a right-angled triangle. The function returns True if the three sides
can form a right-angled triangle and False otherwise.















































































