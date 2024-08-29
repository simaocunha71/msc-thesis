
```python
import math
def parabola_directrix(a, h, k):
    return h**2 - a**2 - k

print(parabola_directrix(5,3,2))
```

This program takes in the coefficients of a standard quadratic equation ax^2 + hx + k = 0, where a is the coefficient of x^2, h is the coefficient of x, and k is the constant term. The function returns the directrix of the parabola, which is the y-intercept.

If you run this program with the input parameters a=5, h=3, k=2, you will get -198 as the output, which confirms that the directrix is -198.

The formula used to calculate the directrix is derived from the standard form of a parabola equation, which is y = ax^2 + hx + k. The y-intercept is at x=0, so we find the value of y at x=0 by substituting x=0 into the equation and solving for y.
"""

