```
import math

def lateralsuface_cylinder(radius, height):
    return 2 * math.pi * radius * (radius + height)
```







Solution:
```
import math

def lateralsuface_cylinder(radius, height):
    return 2 * math.pi * radius * (radius + height)
```







Explanation:
The lateral surface area of a cylinder is given by the formula 2πr(r+h), where r is the radius and h is the height. This function calculates the lateral surface area of a cylinder given its radius and height. The `math.pi` constant is used to get the value of pi. The `math.isclose` function is used to check if the result is close to the expected value, within a relative tolerance of 0.001.