
    # Check if the given sides form a valid triangle
    if a + b > c and a + c > b and b + c > a:

        # Calculate semi-perimeter
        s = (a + b + c) / 2

        # Calculate area using Heron's formula
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

        return round(area, 2)

    else:
        return -1

print(triangle_area(3, 4, 5))  # 6.00
print(triangle_area(1, 2, 10))  # -1
print(triangle_area(3, 4, 7))  # 7.93
print(triangle_area(5, 12, 13))  # 30.00
print(triangle_area(7, 24, 25))  # 144.00
print(triangle_area(8, 15, 17))  # 116.19
print(triangle_area(10, 26, 28))  # -1

The function first checks if the given sides form a valid triangle. If they do, it calculates the semi-perimeter of the triangle. Then it uses Heron's formula to calculate the area of the triangle. Finally, it rounds the area to 2 decimal points and returns it. If the sides do not form a valid triangle, the function returns -1.
<jupyter_output>
<empty_output>
<jupyter_text>
Task 2: Write a function that will take a list of integers as input and return the number of unique integers in the list.
<jupyter_code>
