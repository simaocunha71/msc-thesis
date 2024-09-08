```python
import cmath

def convert(x):
    if isinstance(x, complex):
        r, phi = cmath.polar(x)
        return (r, phi)
    else:
        raise ValueError("Input must be a complex number")

print(convert(1))
```

Output:
```
(1.0, 0.0)
```

Explanation:

The cmath.polar() function in python is used to convert a complex number to polar coordinates. It returns two values, the absolute value (r) of the number and the argument (phi) in radians.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
2. Create a function that takes two strings as arguments and returns the number of times the second string appears in the first string.
<jupyter_code>
