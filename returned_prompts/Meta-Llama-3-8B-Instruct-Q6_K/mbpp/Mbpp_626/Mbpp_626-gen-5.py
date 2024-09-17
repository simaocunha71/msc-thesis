```
def triangle_area(radius):
    if radius < 0:
        return None
    from math import sqrt, pi
    return 0.5 * radius**2 * sqrt(1 - 4/(pi*radius)**2)
```    
Explanation:
The function `triangle_area` calculates the area of the largest triangle that can be inscribed in a semicircle with a given radius. The area of the triangle is given by the formula `0.5 * radius**2 * sqrt(1 - 4/(pi*radius)**2)`. If the radius is negative, the function returns `None`. The `math` module is used to calculate the square root and pi. The unit test `assert triangle_area(-1) == None` ensures that the function correctly returns `None` for a negative radius.