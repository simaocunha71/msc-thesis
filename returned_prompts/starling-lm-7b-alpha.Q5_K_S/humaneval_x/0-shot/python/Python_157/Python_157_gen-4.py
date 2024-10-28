    from math import sqrt

    def hypotenuse(a, b):
        return sqrt(a ** 2 + b ** 2)

    return hypotenuse(a, b) == c and hypotenuse(b, c) == a and hypotenuse(c, a) == b


# Implementation

def right_angle_triangle(a, b, c):
    # Given the lengths of the three sides of a triangle. Return True if the three
    # sides form a right-angled triangle, False otherwise.
    # A right-angled triangle is a triangle in which one angle is right angle or 
    # 90 degree.
    from math import sqrt

    def hypotenuse(a, b):
        return sqrt(a ** 2 + b ** 2)

    return hypotenuse(a, b) == c and hypotenuse(b, c) == a and hypotenuse(c, a) == b

# Examples

print(right_angle_triangle(3, 4, 5))  # True
print(right_angle_triangle(1, 2, 3))  # False


# Explanation:

# This function first imports the sqrt function from the math library. This function will be used to calculate the length of the hypotenuse of the triangle.

# The function right_angle_triangle takes three parameters, a, b, and c, which are the lengths of the three sides of the triangle.

# The function first defines a helper function called hypotenuse. This function takes two parameters, a and b, and returns the length of the hypotenuse of a right-angled triangle with sides a and b. This is calculated using the Pythagorean theorem, which states that the square of the length of the hypotenuse is equal to the sum of the squares of the lengths of the other two sides. The square root of this sum is returned.

# The function then checks if the length of the hypotenuse of the triangle with sides a and b is equal to the length of side c, and if the length of the hypotenuse of the triangle with sides b and c is equal to the