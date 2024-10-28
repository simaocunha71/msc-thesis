```
def triangle_area(radius):
    if radius < 0:
        return None
    semi_circumference = 2 * radius
    side_length = semi_circumference / 2
    area = (1/2) * side_length * radius
    return area
```
The function `triangle_area` calculates the area of the largest triangle that can be inscribed in a semicircle with a given radius. If the radius is negative, it returns `None`. 

The area of the triangle is calculated using the formula `(1/2) * base * height`, where the base is the side length of the semicircle, and the height is the radius of the semicircle.

The unit test `assert triangle_area(-1) == None` ensures that the function returns `None` when the radius is negative. 

Note: The area of the triangle is calculated using the formula `(1/2) * side_length * radius`, where `side_length` is half of the semi-circumference of the semicircle. This is because the triangle is inscribed in the semicircle, and the base of the triangle is the side length of the semicircle. The height of the triangle is the radius of the semicircle. 

The `semi_circumference` is calculated as `2 * radius`, and the `side_length` is calculated as `semi_circumference / 2`, because the side length of the semicircle is half of its circumference. 

The function returns the calculated area. 

This function assumes that the input radius is a non-negative number. If the input radius is negative, the function returns `None`. 

The time complexity of this function is O(1), because it performs a constant amount of work regardless of the size of the input. The space complexity is also O(1), because it uses a constant amount of space to store the variables. 