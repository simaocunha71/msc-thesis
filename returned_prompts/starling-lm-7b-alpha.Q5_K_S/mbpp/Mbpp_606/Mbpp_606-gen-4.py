"""
from math import pi
def radian_degree(degree):
    return degree*pi/180
"""

def radian_degree(degree):
    return degree*math.pi/180

def test_radian_degree():
    assert radian_degree(90)==1.5707963267948966
test_radian_degree()


"""
"""
def radian_degree(degree):
    pi = 3.14159265358979323846
    return degree*pi/180
"""

```

In this case, the function `radian_degree` converts degrees to radians. It multiplies the input `degree` by the value of `pi` divided by 180. The test case checks if the function correctly converts 90 degrees to the expected value of 1.5707963267948966 radians.

To use the function, you can call `radian_degree` with the desired degree value as the argument. For example, `radian_degree(90)` will return `1.5707963267948966`.

Please note that the `math.pi` constant is used to calculate the conversion factor. If you are not using a library that provides this constant, you can define `pi` as `3.14159265358979323846` and use it in the function instead.

The provided test case `test_radian_degree()` asserts that the function returns the expected result for the given test case. You can add more test cases to further validate the function's correctness.

Overall, this function and test case ensure that the conversion from degrees to radians is accurate and reliable.
```