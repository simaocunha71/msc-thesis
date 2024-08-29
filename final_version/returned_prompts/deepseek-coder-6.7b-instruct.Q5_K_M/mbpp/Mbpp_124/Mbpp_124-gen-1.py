Here is the function:

```python
import cmath

def angle_complex(z):
    return cmath.phase(z)
```

This function uses the `phase` function from the `cmath` module to compute the phase of a complex number, which is equivalent to the angle of a complex number.

Note: The phase is in radians and it's in the range [-pi, pi]. If you want to get the angle in degrees, you can multiply by 180/pi.

Test the function:

```python
print(math.isclose(angle_complex(0+1j), 1.5707963267948966, rel_tol=0.001))
```

This should return `True`.

This function works by first converting the complex number to its polar form using the `cmath.polar` function, which returns a tuple `(r, phi)` where `r` is the absolute value of the complex number and `phi` is the phase. The phase is then returned by the function.

The `math.isclose` function is used to compare the computed phase with the expected phase, with a relative tolerance of 0.001.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
