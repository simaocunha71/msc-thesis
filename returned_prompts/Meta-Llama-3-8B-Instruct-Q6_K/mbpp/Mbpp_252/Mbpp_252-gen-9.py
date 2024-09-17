```
def convert(c):
    r = abs(c)
    phi = cmath.phase(c)
    return r, phi
```


This Python function takes a complex number `c` as input and returns its polar coordinates as a tuple `(r, phi)`. The `r` is the magnitude (or modulus) of the complex number and `phi` is the argument (or phase) of the complex number. 

We use the built-in `abs` function to calculate the magnitude and `cmath.phase` function to calculate the argument of the complex number. The function is tested with the unit test `assert convert(1) == (1.0, 0.0)`, which checks if the function correctly converts the real number 1 to its polar coordinates (1.0, 0.0). 

Note that the `cmath` module is required for this function to work as it provides the `phase` function, which is used to calculate the argument of a complex number. 

The function does not handle any exceptions or edge cases. In a real-world application, you would want to add error checking to handle cases where the input is not a complex number, or where the complex number is zero or infinity. 

Here is a more robust version of the function that includes some basic error checking:

```
import cmath

def convert(c):
    if not isinstance(c, complex):
        raise ValueError("Input must be a complex number")
    if c == 0:
        raise ValueError("Input cannot be zero")
    r = abs(c)
    phi = cmath.phase(c)
    return r, phi
``` 







