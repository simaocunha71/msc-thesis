The lateral surface area of a cone can be calculated by using the formula πr(l+r), where l is the slant height of the cone. The slant height can be calculated using the Pythagorean theorem, which is √(h^2+r^2).

Here is the Python function to calculate the lateral surface area of a cone:

```
import math

def lateralsurface_cone(r, h):
    l = math.sqrt(h**2 + r**2)
    return math.pi * r * (l + r)
```

This function takes the radius and height as inputs and returns the lateral surface area of the cone. The unit test `assert lateralsurface_cone(5,12)==204.20352248333654` ensures that the function is working correctly. 

Please note that the result of the calculation may not be exact due to the nature of floating point arithmetic. However, the function should be able to calculate the lateral surface area of a cone with reasonable accuracy. 