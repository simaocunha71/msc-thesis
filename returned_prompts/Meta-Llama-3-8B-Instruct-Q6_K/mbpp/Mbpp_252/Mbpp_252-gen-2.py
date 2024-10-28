```
def convert(complex_num):
    if isinstance(complex_num, complex):
        r = abs(complex_num)
        theta = cmath.phase(complex_num)
        return (r, theta)
    else:
        raise TypeError("Input must be a complex number")
```


In this function, we first check if the input is a complex number using the isinstance() function. If it is, we calculate the modulus (radius) using the abs() function and the phase (angle) using the cmath.phase() function from the cmath module. If the input is not a complex number, we raise a TypeError. The function returns a tuple containing the radius and angle. The unit test `assert convert(1) == (1.0, 0.0)` checks that the function works correctly for a real number (in this case, the complex number 1 is equivalent to the real number 1, so the output should be (1, 0)). The unit test also checks that the function works correctly for a complex number. If the input is not a complex number, the function should raise a TypeError.