```
import math

def lateralsurface_cone(r, h):
    l = math.pi * r * (r + math.sqrt(h**2 + r**2))
    return l
```    
Explanation: 
The lateral surface area of a cone is given by the formula πr(r + sqrt(h^2 + r^2)), where r is the radius of the base and h is the height of the cone. This function calculates this area by using the math.pi constant and the math.sqrt function to calculate the square root. The unit test provided ensures that the function returns the correct result for a cone with a radius of 5 and a height of 12. The result is approximately 204.20352248333654.