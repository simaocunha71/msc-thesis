```
def triangle_area(radius):
    if radius < 0:
        return None
    return 0.5 * radius * (radius * 2 ** 0.5)
```    
Explanation:
The area of a triangle inscribed in a semicircle with a given radius can be calculated using the formula `(1/2) * base * height`. In this case, the base is equal to the diameter of the semicircle (which is `2 * radius`) and the height is the length of the altitude from the center of the semicircle to the base of the triangle, which is equal to `radius * sqrt(2)`. 

The function first checks if the radius is negative, in which case it returns `None` as per the problem statement. If the radius is non-negative, it calculates the area of the triangle using the formula and returns it. 

The unit test `assert triangle_area(-1) == None` ensures that the function returns `None` when the radius is negative. This is because a triangle cannot be inscribed in a semicircle with a negative radius. 

Note: The `** 0.5` is used to calculate the square root. It is equivalent to `math.sqrt(2)` but is more concise. However, in Python 3.8 and later, you can use `math.sqrt(2)` for better readability. 

This solution assumes that the radius is not negative. If the radius can be negative and you want to handle this case, you can add a check at the beginning of the function and return a specific value (e.g., `None`) or raise an exception. 

Also, the solution does not handle the case where the radius is zero. If you want to handle this case, you can add a check at the beginning of the function and return a specific value (e.g., `0`) or raise an exception. 

Finally, the solution assumes that the semicircle is a circle with a diameter equal to the given radius. If the semicircle has a different diameter, you need to adjust the formula accordingly. 

In summary, this solution is a simple and efficient way to calculate the area of the largest triangle that can be inscribed in a semicircle with a given radius. It is easy to understand and use, and it handles the edge cases correctly. However, it may not be suitable for all cases, and you need to consider the specific requirements of your problem before using this solution. 