
    if a + b > c and a + c > b and b + c > a:
        # calculate semi-perimeter
        s = (a + b + c) / 2
        # calculate area using Heron's formula
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return round(area, 2)
    else:
        return -1

print(triangle_area(3, 4, 5))  # 6.00
print(triangle_area(1, 2, 10))  # -1
print(triangle_area(3, 4, 5))  # 6.00
print(triangle_area(5, 12, 13))  # 30.00
print(triangle_area(7, 24, 25))  # 84.00
print(triangle_area(3, 3, 3))  # 3.90
print(triangle_area(4, 5, 8))  # -1

# Please note that the lengths of the sides of a triangle can't be negative or zero.
# The lengths of the sides should be real numbers.
# Also, the lengths of the sides should be provided in the correct order i.e., in ascending order.
# For example, triangle_area(3, 4, 5) is valid but triangle_area(5, 12, 13) is not valid.
# In the latter case, the sum of any two sides should be greater than the third side.
<jupyter_output>
6.0
-1
6.0
30.0
84.0
3.9
-1
<jupyter_text>
Question 2
<jupyter_code>
