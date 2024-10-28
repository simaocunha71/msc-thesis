```
def triangle_area(radius):
    if radius < 0:
        return None
    return radius**2 / 2
```


The problem asks to find the area of the largest triangle that can be inscribed in a semicircle with a given radius. 

The area of the triangle can be calculated using the formula (base * height) / 2. In this case, the base of the triangle is the diameter of the semicircle, which is 2 * radius. The height of the triangle is the height from the base to the center of the semicircle, which is radius. 

The unit test `assert triangle_area(-1) == None` suggests that the function should return None when the radius is negative. This is because a semicircle cannot have a negative radius.

Here is the Python function that solves the problem:

```
def triangle_area(radius):
    if radius < 0:
        return None
    return radius**2 / 2
```


This function takes a radius as input, checks if it is negative, and returns the area of the triangle if it is not negative. If it is negative, the function returns None. The area of the triangle is calculated using the formula (base * height) / 2, where the base is 2 * radius and the height is radius. The result is returned as the output of the function.