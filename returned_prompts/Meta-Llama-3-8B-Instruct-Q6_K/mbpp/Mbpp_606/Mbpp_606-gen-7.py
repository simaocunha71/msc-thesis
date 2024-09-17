```
def radian_degree(degrees):
    pi = 3.14159265359
    return degrees * (pi / 180)
```



Here is the explanation of the code:

The function radian_degree takes a degree as an input and returns the equivalent radian.

We use the mathematical conversion formula: 1 degree = pi/180 radians.

So, we multiply the input degree by pi/180 to get the equivalent radian.

The unit test `assert radian_degree(90)==1.5707963267948966` helps to verify that the function is working correctly. For example, 90 degrees is equivalent to 1.5707963267948966 radians.

This function can be used to convert degrees to radians for any given degree. For example, radian_degree(180) would return 3.14159265359 radians.