```
def radian_degree(degrees):
    import math
    return math.pi * degrees / 180
```


This problem is asking to create a function that converts degrees to radians. The unit test provided is `assert radian_degree(90)==1.5707963267948966`, which helps to understand the conversion ratio. The ratio is pi / 180, which is used in the function. The function takes an angle in degrees as input and returns the equivalent angle in radians. The math library is used to get the value of pi. 

The unit test `assert radian_degree(90)==1.5707963267948966` is passing because the function is correctly converting 90 degrees to radians. The result of this conversion is approximately 1.5707963267948966 radians. 

The function is then used to convert any given angle in degrees to radians. For example, `radian_degree(180)` would return approximately 3.141592653589793 radians. 