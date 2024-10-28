```
def radian_degree(deg):
    return deg * 3.141592653589793/180
```


The problem is asking to create a function that converts a given degree value into its equivalent radian value. 

The function should take an angle in degrees as an argument and return the equivalent angle in radians. 

For example, if the input is 90 degrees, the output should be approximately 1.5707963267948966 radians.

The unit test provided helps in understanding the problem better. The test `assert radian_degree(90)==1.5707963267948966` indicates that the function should convert 90 degrees to radians and return the result as 1.5707963267948966.

Here is the solution:
```
def radian_degree(deg):
    return deg * 3.141592653589793/180
```
This function takes an angle in degrees as an argument, multiplies it by the conversion factor (pi/180), and returns the result as the equivalent angle in radians. 

For example, if the input is 90 degrees, the function will return 1.5707963267948966 radians, which is the correct conversion. 

The unit test provided will pass with this function. 

The function can be used to convert any angle from degrees to radians, not just 90 degrees. It is a general-purpose conversion function. 