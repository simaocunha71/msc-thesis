```
def triangle_area(radius):
    if radius < 0:
        return None
    return 0.5 * radius ** 2
```
The problem is asking to find the area of the largest triangle that can be inscribed in a semicircle with a given radius. 

The solution is to return half the square of the radius, since the area of the triangle is half the base times the height. The base is the diameter of the semicircle, which is equal to the radius multiplied by 2. The height is the radius itself.

The unit test `assert triangle_area(-1) == None` is used to handle the edge case where the radius is negative. In this case, the function should return `None`. This is because the problem doesn't specify what to do when the radius is negative, and it's a common convention in mathematics to return `None` or an error in such cases. 

The function `triangle_area` takes a radius as input, and returns the area of the largest triangle that can be inscribed in a semicircle with that radius. If the radius is negative, it returns `None`. Otherwise, it returns `0.5 * radius ** 2`. This is the area of the triangle, since the base is the diameter of the semicircle, which is `2 * radius`, and the height is the radius itself. The area of the triangle is half the base times the height, which is `0.5 * (2 * radius) * radius = 0.5 * radius ** 2`. 