```
import math

def lateralsurface_cone(r, h):
    return math.pi*r*(math.sqrt(r**2+h**2))
```


The problem asks to write a function that calculates the lateral surface area of a cone given its radius and height. The lateral surface area of a cone is given by the formula πr√(r²+h²), where r is the radius and h is the height of the cone.

The unit test `assert lateralsurface_cone(5,12)==204.20352248333654` helps to verify the correctness of the function.

Here's a Python solution for the problem:

```
import math

def lateralsurface_cone(r, h):
    return math.pi*r*(math.sqrt(r**2+h**2))
```

This function takes two arguments, the radius `r` and the height `h`, and returns the lateral surface area of the cone. It uses the math module to calculate the value of π and the square root. The formula is then applied to calculate the lateral surface area.