    from math import sqrt
    # Hypotenuse is the longest side of the right angle triangle. It is the side opposite the right angle.
    # Pythagorean Theorem states that the square of the hypotenuse (c) is equal to the sum of the squares of the other two sides (a and b).
    # c**2 = a**2 + b**2
    hypotenuse = sqrt(a**2 + b**2)
    return hypotenuse == c

# Test Cases
print(right_angle_triangle(3, 4, 5))   # True
print(right_angle_triangle(1, 2, 3))   # False
print(right_angle_triangle(5, 12, 13)) # True
print(right_angle_triangle(8, 15, 17)) # False





def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    """
    # Hypotenuse is the longest side of the right angle triangle. It is the side opposite the right angle.
    # Pythagorean Theorem states that the square of the hypotenuse (c) is equal to the sum of the squares of the other two sides (a and b).
    # c**2 = a**2 + b**2
    hypotenuse = (a**2 + b**2)**(1/2)
    return hypotenuse == c

# Test Cases
print(right_angle_triangle(3, 4, 5))   # True
print(right_angle_triangle(1, 2, 3))   # False
print(right_angle_triangle(5, 12, 13)) #