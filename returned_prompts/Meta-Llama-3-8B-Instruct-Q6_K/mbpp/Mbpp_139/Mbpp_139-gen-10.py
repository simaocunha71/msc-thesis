```
import math

def circle_circumference(radius):
    return 2 * math.pi * radius
```
In this solution, we use the mathematical constant pi from the math module and multiply it by the radius of the circle to calculate the circumference. The unit test provided ensures that the function is working correctly. The test uses the math.isclose function to compare the calculated circumference with the expected result, considering a small tolerance for floating point precision errors. The expected result is 62.83 for a circle with a radius of 10. The function is then tested with the radius 10 and the calculated circumference is 62.83 which is close to the expected result. 