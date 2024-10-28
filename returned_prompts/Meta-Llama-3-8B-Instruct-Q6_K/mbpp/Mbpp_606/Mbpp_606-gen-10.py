```
def radian_degree(degree):
    return degree * 3.141592653589793/180
```



This function takes a degree as input and returns the equivalent radian value. The conversion is done by multiplying the input degree by π/180, which is a common mathematical constant representing the ratio of a circle's circumference to its diameter. The result is a radian value. The unit test `assert radian_degree(90) == 1.5707963267948966` confirms the correctness of the function.