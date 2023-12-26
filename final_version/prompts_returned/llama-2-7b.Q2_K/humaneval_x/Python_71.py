
def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    
    # a < b + c or a > b and (a,b,c) is a valid triangle --> return area of triangle with a > b and (a,b,c) is a valid triangle
    if ((a <= b+c) or (b >= 10*2)) :  # if sum < sum of any two sides then return -1
        return -1.0  
    else:
        return math.pi * a * c / 3.0