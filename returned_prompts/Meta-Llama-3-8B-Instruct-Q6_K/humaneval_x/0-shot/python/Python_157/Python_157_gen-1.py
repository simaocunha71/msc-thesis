    # This function checks if the given sides can form a right-angled triangle
    # by checking if the square of the length of the hypotenuse is equal to
    # the sum of the squares of the other two sides.
    def is_right_angle(a, b, c):
        # Check if a, b, c are sides of a triangle
        if a + b <= c or a + c <= b or b + c <= a:
            return False
        # Check if the square of the length of the hypotenuse is equal to
        # the sum of the squares of the other two sides
        return a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2

    return is_right_angle(a, b, c)  # Call the helper function and return the result.  # noqa: E501
    # This function is called with three parameters (a, b, c) which are the sides
    # of a triangle. It first checks if these sides can form a triangle by
    # checking if the sum of the lengths of any two sides is greater than the
    # length of the third side. If they can form a triangle, it checks if the
    # square of the length of the hypotenuse is equal to the sum of the squares
    # of the other two sides. If this condition is met, it returns True, meaning
    # that the sides form a right-angled triangle. Otherwise, it returns False.
    # The helper function is_right_angle(a, b, c) is used to check if the sides
    # can form a right-angled triangle. It checks if a, b, c are sides of a
    # triangle, and then checks if the square of the length of the hypotenuse
    # is equal to the sum of the squares of the other two sides. If both
    # conditions are met, it returns True. Otherwise, it returns False.  # noqa: E501
    # The helper function is_right_angle(a, b, c) is used to check if the sides
    # can form a right-angled triangle. It checks if a, b, c are sides of a
    # triangle, and then checks if the square of the length of the hypotenuse
    # is equal to the sum of the squares