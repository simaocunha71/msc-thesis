
    # check if the three sides can form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        # calculate the area using Heron's formula
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1


print(triangle_area(3, 4, 5))  # 6.00
print(triangle_area(1, 2, 10))  # -1

'''
Heron's formula:
The area of a triangle whose sides have lengths a, b, and c is given by:
Area = √[s(s - a)(s - b)(s - c)]
where s is the semi-perimeter of the triangle given by:
s = (a + b + c) / 2
'''

'''
In this solution, the first thing we do is to check if the three sides can form a valid triangle. 
If they can't, we return -1.

If they can, we calculate the semi-perimeter of the triangle.

Finally, we use Heron's formula to calculate the area of the triangle.
We round the area to 2 decimal places before returning it.
'''

# 