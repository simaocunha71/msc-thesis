```
def triangle_area(radius):
    if radius <= 0:
        return None
    half_radius = radius / 2
    side_length = (2 ** 0.5 - 1) * half_radius
    height = half_radius * (2 ** 0.5)
    area = 0.5 * side_length * height
    return area
```
The problem is to find the area of the largest triangle that can be inscribed in a semicircle with a given radius. 

The area of the largest triangle that can be inscribed in a semicircle with a given radius can be calculated using the formula: `0.5 * side_length * height`. The `side_length` is the length of the side of the triangle, and the `height` is the height of the triangle.

We can calculate the `side_length` and `height` using the following formulas: `side_length = (2 ** 0.5 - 1) * half_radius` and `height = half_radius * (2 ** 0.5)`, where `half_radius` is half of the given radius.

The function takes a radius as input and returns the area of the largest triangle that can be inscribed in a semicircle with that radius. If the radius is less than or equal to 0, the function returns `None`.

The unit test `assert triangle_area(-1) == None` ensures that the function returns `None` when the radius is less than or equal to 0. This is because a semicircle with a radius less than or equal to 0 does not exist.