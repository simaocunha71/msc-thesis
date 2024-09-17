```
import math

def volume_cone(radius, height):
    volume = (1/3) * math.pi * (radius ** 2) * height
    return volume
```


The provided unit test ensures that the function is accurate within a relative tolerance of 0.001. This means that the result should be close to the expected value, but not necessarily exactly equal due to floating-point precision issues. The expected value is calculated using the formula for the volume of a cone, which is (1/3)πr²h, where r is the radius and h is the height. The function takes two parameters, radius and height, and returns the calculated volume. The math.isclose function is used to compare the result with the expected value, allowing for a small difference due to floating-point precision. The function should be able to handle different inputs and provide accurate results within the specified tolerance. 