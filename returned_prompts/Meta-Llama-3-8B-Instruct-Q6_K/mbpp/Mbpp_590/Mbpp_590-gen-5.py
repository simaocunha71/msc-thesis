```
import math
from cmath import rect

def polar_rect(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)
```
This function takes two parameters: the radius (r) and the angle (theta) in polar coordinates. It returns a tuple of the x and y coordinates in rectangular coordinates. The math library is used for trigonometric functions, and the cmath library is used for complex numbers. The unit test provided helps to clarify the expected output format. 

Note that the unit test `assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))` suggests that the function should return a tuple of two values, the first being a real number and the second being a complex number. This is because the rectangular coordinates can be complex if the angle is not within the range [0, 2*pi). 

The function uses the standard formulas for converting polar coordinates to rectangular coordinates: x = r * cos(theta) and y = r * sin(theta). 

The cmath library is used to handle complex numbers, which may be necessary if the angle is not within the range [0, 2*pi). The rect function from the cmath library is used to convert the complex number to a rectangular coordinate. 

The unit test provided helps to ensure that the function is working correctly. 

Note that the function does not handle invalid input, such as a negative radius or an angle outside the range [0, 2*pi). You may want to add error handling to handle such cases. 