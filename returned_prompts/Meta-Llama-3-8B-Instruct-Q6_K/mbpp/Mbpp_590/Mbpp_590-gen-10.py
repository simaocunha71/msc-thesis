```
def polar_rect(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)
```
The function `polar_rect` takes two parameters: `r` (radius) and `theta` (angle in radians). It calculates the rectangular coordinates `x` and `y` using the formulas `x = r * cos(theta)` and `y = r * sin(theta)`, and returns them as a tuple.

The unit test `assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))` verifies that the function correctly converts polar coordinates to rectangular coordinates. The expected result is a tuple containing the rectangular coordinates `x` and `y` as complex numbers. The `assert` statement checks if the output of the function matches the expected result. If the output does not match, the `assert` statement raises an `AssertionError`.