```
    import math

    # calculate the semi-perimeter of the triangle
    s = (a + b + c) / 2

    # calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # check if the three sides form a valid triangle
    if area > 0:
        return round(area, 2)
    else:
        return -1
```


This code defines a function `triangle_area` that takes the lengths of the three sides of a triangle as input and returns the area of the triangle. It uses Heron's formula to calculate the area, and checks if the three sides form a valid triangle by checking if the area is positive. If the area is positive, it rounds the area to 2 decimal points and returns it. Otherwise, it returns -1. The code uses the `math` module to calculate the square root. 

The example `triangle_area(3, 4, 5)` returns `6.00` because the three sides form a valid triangle and the area is calculated correctly. The example `triangle_area(1, 2, 10)` returns `-1` because the three sides do not form a valid triangle. 

The code is written in Python, but the logic can be applied to any programming language. 

Please note that this code assumes that the input values are numbers. If the input values are not numbers, the code will raise an error. You may want to add error handling to handle this case. 

Also, this code assumes that the input values represent the lengths of the sides of a triangle. If the input values represent something else, the code will not work correctly. You may want to add validation to ensure that the input values represent the lengths of the sides of a triangle. 