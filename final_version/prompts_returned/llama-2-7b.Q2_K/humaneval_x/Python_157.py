
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    if b * c > a**2:
        return False
    else:
        return True

if __name__ == '__main__':
    print("right angled triangle test case 0")
    print(right_angle_triangle(3, 4, 5))
    
    print("right angled triangle test case 1")
    print(right_angle_triangle(2, 4, 3))
