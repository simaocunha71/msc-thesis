```
import math

def volume_cone(radius, height):
    volume = (1.0/3) * math.pi * radius**2 * height
    return volume
```


This function takes two parameters: the radius of the cone's base and the height of the cone. It uses the formula for the volume of a cone, which is `(1/3) * π * r^2 * h`, where `r` is the radius and `h` is the height. The result is returned by the function.

The unit test `assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)` checks if the function returns the correct volume for a cone with a radius of 5 and a height of 12. The `math.isclose` function is used to compare the result with the expected value, with a relative tolerance of 0.001. This means that the result is considered correct if it is within 0.1% of the expected value.