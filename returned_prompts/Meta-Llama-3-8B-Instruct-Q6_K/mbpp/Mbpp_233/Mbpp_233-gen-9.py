```
import math

def lateralsuface_cylinder(radius, height):
    lateral_surface_area = 2 * math.pi * radius * (radius + height)
    return lateral_surface_area
```


The problem is to write a function that calculates the lateral surface area of a cylinder. The lateral surface area is the area of the curved surface of the cylinder. 

The function should take two parameters: the radius of the cylinder and its height. 

The unit test provided is `assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)`. This test case is checking if the lateral surface area of a cylinder with a radius of 10 and a height of 5 is approximately equal to 314.15.

Here's the solution:
```
import math

def lateralsuface_cylinder(radius, height):
    lateral_surface_area = 2 * math.pi * radius * (radius + height)
    return lateral_surface_area
```
This function uses the formula for the lateral surface area of a cylinder, which is `2 * pi * r * (r + h)`, where `r` is the radius and `h` is the height. The `math.pi` constant is used to get the value of pi. The function returns the calculated lateral surface area. 

The unit test provided checks if the function returns the correct result for a cylinder with a radius of 10 and a height of 5. The `math.isclose` function is used to compare the calculated result with the expected result, allowing for a small tolerance due to floating point precision errors. 

You can use this function to calculate the lateral surface area of any cylinder by providing the radius and height as arguments. For example, `lateralsuface_cylinder(5, 10)` would calculate the lateral surface area of a cylinder with a radius of 5 and a height of 10. 