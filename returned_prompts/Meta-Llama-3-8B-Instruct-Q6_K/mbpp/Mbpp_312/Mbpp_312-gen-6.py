```
import math

def volume_cone(radius, height):
    volume = (1/3) * math.pi * radius**2 * height
    return volume
```


This function calculates the volume of a cone using the formula (1/3) * π * r^2 * h, where r is the radius and h is the height of the cone. The function takes two parameters: radius and height. It returns the volume of the cone. The unit test provided ensures that the function returns the correct result for a cone with a radius of 5 and a height of 12. The test uses the close() function from the math module to check if the result is close to the expected value within a relative tolerance of 0.001.