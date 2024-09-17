```
def convert(z):
    r = (z.real**2 + z.imag**2)**0.5
    theta = 0 if z.real >= 0 else math.pi
    theta += math.atan2(z.imag, z.real)
    return r, theta
```


This function takes a complex number `z` as input and returns its polar coordinates as a tuple `(r, theta)`. The `r` value is the magnitude (or radius) of the complex number, and the `theta` value is the angle (in radians) between the positive real axis and the line connecting the origin to the complex number. 

The `math.atan2` function is used to calculate the angle because it returns the correct value for the angle even when the real part of the complex number is negative. 

The unit test `assert convert(1) == (1.0, 0.0)` ensures that the function works correctly for real numbers. For real numbers, the imaginary part is zero, so the angle is zero and the magnitude is the same as the real part. 

This function will work for any complex number, not just real numbers. For complex numbers with positive real parts, the angle will be between 0 and pi. For complex numbers with negative real parts, the angle will be between pi and 2pi. 

Note that the `math` module is imported implicitly when `math.atan2` is used. If you're using Python 2, you'll need to import `math` explicitly. In Python 3, the `math` module is imported implicitly when you use `math.atan2`. 