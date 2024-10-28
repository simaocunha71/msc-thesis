```
import math

def lateralsuface_cylinder(radius, height):
    return 2 * math.pi * radius * (radius + height)
```


The problem asks to write a function that calculates the lateral surface area of a cylinder. The lateral surface area is the area of the curved part of the cylinder, excluding the top and bottom circular surfaces.

The function should take two parameters: the radius of the cylinder and its height. 

The unit test provided ensures that the function is correct by comparing the result of the function with the expected result. The expected result is calculated using the formula for the lateral surface area of a cylinder, which is `2 * pi * r * (r + h)`, where `r` is the radius and `h` is the height.

Here is the solution in Python:

```
import math

def lateralsuface_cylinder(radius, height):
    return 2 * math.pi * radius * (radius + height)
```

This function uses the formula for the lateral surface area of a cylinder to calculate the result. The `math.pi` constant is used to get the value of pi, and the `*` operator is used to multiply the values together. The result is returned as the output of the function.