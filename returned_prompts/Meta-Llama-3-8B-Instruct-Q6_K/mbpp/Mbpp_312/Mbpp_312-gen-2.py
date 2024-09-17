```
import math

def volume_cone(radius, height):
    return (1/3) * math.pi * radius**2 * height
```


Explanation:
The problem is asking to write a function that calculates the volume of a cone. The volume of a cone is given by the formula (1/3) * π * r^2 * h, where r is the radius of the base and h is the height of the cone.

The unit test provided ensures that the function is working correctly. It checks that the function returns the expected volume for a cone with a radius of 5 and a height of 12. The `math.isclose` function is used to compare the result with the expected value, taking into account a small tolerance for floating-point precision errors.

The solution simply implements the formula for the volume of a cone using the provided radius and height. The `math.pi` constant is used to represent the mathematical constant pi. The `**` operator is used to raise the radius to the power of 2. The result is returned by the function.