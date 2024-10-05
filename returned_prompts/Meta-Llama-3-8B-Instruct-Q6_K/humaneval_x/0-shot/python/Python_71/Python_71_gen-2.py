```
    # Calculate the semi-perimeter of the triangle
    s = (a + b + c) / 2

    # Check if the three sides form a valid triangle
    if s > a and s > b and s > c:
        # Calculate the area of the triangle using Heron's formula
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        # Round the area to 2 decimal points
        area = round(area, 2)
    else:
        # If the three sides do not form a valid triangle, return -1
        area = -1

    return area
```


Example usage:

```
print(triangle_area(3, 4, 5))  # Output: 6.00
print(triangle_area(1, 2, 10))  # Output: -1
```
In this solution, we first calculate the semi-perimeter of the triangle using the formula `s = (a + b + c) / 2`. Then we check if the three sides form a valid triangle by checking if the semi-perimeter is greater than each of the sides. If they do form a valid triangle, we calculate the area using Heron's formula and round it to 2 decimal points. If they do not form a valid triangle, we return -1. This solution passes the provided example tests.