```
import math

def lateralsurface_cone(r, h):
    slant_height = math.sqrt(r**2 + h**2)
    lateral_surface_area = math.pi * r * slant_height
    return lateral_surface_area
```






```
import math

def lateralsurface_cone(r, h):
    slant_height = math.sqrt(r**2 + h**2)
    lateral_surface_area = math.pi * r * slant_height
    return lateral_surface_area
```


This function calculates the lateral surface area of a cone given the radius r and the height h. The lateral surface area of a cone is given by the formula pi*r*slant_height, where slant_height is the distance from the center of the cone to the circumference. This is calculated using the Pythagorean theorem, sqrt(r^2 + h^2). The function then returns the calculated lateral surface area. 

The unit test provided ensures that the function produces the correct result for a specific set of inputs, which is a radius of 5 and a height of 12. This test is used to verify that the function is working correctly. 

The function is simple and easy to understand, and it accurately calculates the lateral surface area of a cone given the radius and height.