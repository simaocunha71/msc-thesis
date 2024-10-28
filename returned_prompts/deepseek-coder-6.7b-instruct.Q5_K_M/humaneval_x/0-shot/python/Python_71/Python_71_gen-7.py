
    # check if it's a valid triangle
    if (a + b > c) and (a + c > b) and (b + c > a):
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        # calculate the area
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return round(area, 2)
    else:
        return -1

print(triangle_area(3, 4, 5))  # 6.00
print(triangle_area(1, 2, 10))  # -1
print(triangle_area(3, 4, 7))  # 6.00
print(triangle_area(5, 12, 13))  # 30.00
print(triangle_area(7, 24, 25))  # 84.00

# 3 sides of a right triangle can form a valid triangle
print(triangle_area(3, 4, 5))  # 6.00
# 2 sides of a triangle are equal
print(triangle_area(3, 3, 3))  # 3.90
# 1 side of a triangle is equal to the sum of the other two
print(triangle_area(1, 2, 3))  # -1
# negative sides are not allowed
print(triangle_area(-1, 2, 3))  # -1
# all sides are zero
print(triangle_area(0, 0, 0))  # -1
# one side is zero
print(triangle_area(3, 4, 0))  # -1

'''
The function works by first checking if the given lengths can form a valid triangle.
If they can, it calculates the semi-perimeter and uses Heron's formula to find the area.
The area is then rounded to 2 decimal points and returned. If the lengths cannot form
a valid triangle, the function returns -1.
'''
<jupyter_output>
6.0
-1
6.0
30.0
