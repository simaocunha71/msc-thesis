```
    import math

    # check if the three sides form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        # calculate the area
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        # round the area to 2 decimal points
        area = round(area, 2)
        return area
    else:
        return -1
```


This function first checks if the three sides form a valid triangle by checking if the sum of any two sides is greater than the third side. If they do, it calculates the semi-perimeter and then uses Heron's formula to calculate the area of the triangle. The area is then rounded to 2 decimal points. If the three sides do not form a valid triangle, the function returns -1. 

Note that this function assumes that the input sides are non-negative. If negative sides are possible, the function would need to handle that case. Also, the function uses the math module to calculate the square root, so the math module needs to be imported. 

The unit test `triangle_area(3, 4, 5) == 6.00` ensures that the function returns the correct area for a valid triangle. The unit test `triangle_area(1, 2, 10) == -1` ensures that the function returns -1 for a set of sides that do not form a valid triangle. 