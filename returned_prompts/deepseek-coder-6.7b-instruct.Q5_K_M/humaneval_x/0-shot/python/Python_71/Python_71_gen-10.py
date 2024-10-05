
    if (a < b + c) and (b < a + c) and (c < a + b):
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        # calculate the area using Heron's formula
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return round(area, 2)
    else:
        return -1

# Test cases
print(triangle_area(3, 4, 5))  # 6.00
print(triangle_area(1, 2, 10))  # -1
print(triangle_area(3, 4, 6))  # 5.33
print(triangle_area(5, 12, 13))  # 30.00
print(triangle_area(7, 24, 25))  # 84.00
<jupyter_output>
6.0
-1
5.33
30.0
84.0
<jupyter_text>
Problem 3
<jupyter_code>
