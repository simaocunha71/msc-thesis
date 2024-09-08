"""
The formula to calculate the area of a triangle given its three sides is 
sqrt(s*(s-a)*(s-b)*(s-c)) 
where s is the semi-perimeter of the triangle, given by s = (a+b+c)/2.

For a semicircle, the largest possible triangle it can contain has its diameter as its base and the radius as its height. Therefore, its area is given by 1/2 * radius * diameter.

However, if the radius is negative, it is not possible to create a semicircle with negative radius. Therefore, the function should return None for such cases.
"""

Solution:

def triangle_area(radius):
    if radius < 0:
        return None
    else:
        diameter = 2 * radius
        area = 0.5 * radius * diameter
        return area
"""

assert triangle_area(-1) == None
"""

