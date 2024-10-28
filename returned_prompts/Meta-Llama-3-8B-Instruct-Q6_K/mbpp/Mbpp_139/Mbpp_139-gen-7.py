```
import math

def circle_circumference(radius):
    return 2 * math.pi * radius
```


Note: The unit test provided checks for the circumference of a circle with a radius of 10. It's expected to be close to 62.83. The provided solution calculates the circumference using the formula 2 * pi * radius. The math.isclose function is used to check for the closeness of the calculated value to the expected value. The relative tolerance is set to 0.001 to account for floating point precision errors.