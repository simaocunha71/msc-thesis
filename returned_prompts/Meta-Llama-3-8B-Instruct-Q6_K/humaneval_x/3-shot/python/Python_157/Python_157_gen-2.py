    sides = sorted([a, b, c])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False
    # This function first sorts the sides of the triangle. Then checks if the sum of 
    # the squares of the two shorter sides is equal to the square of the longest side. 
    # If it is, then the triangle is a right-angled triangle and the function returns True. 
    # Otherwise, it returns False. 
    # The ** operator is used to calculate the square of a number. For example, 
    # a**2 is equivalent to a * a. 
    # The sides[0]**2 + sides[1]**2 == sides[2]**2 condition is the Pythagorean 
    # theorem, which is a fundamental concept in geometry and is used to test if a 
    # triangle is right-angled. The Pythagorean theorem states that for a right-angled 
    # triangle, the square of the length of the hypotenuse (the longest side) is equal 
    # to the sum of the squares of the lengths of the other two sides. 
    # For example, if you have a right-angled triangle with one side of length 3, 
    # one side of length 4, and one side of length 5, then the sum of the squares of 
    # the two shorter sides (3**2 + 4**2 = 9 + 16 = 25) is equal to the square of 
    # the longest side (5**2 = 25), so the triangle is a right-angled triangle. 
    # The function is case-insensitive and works with any three positive numbers. 
    # For example, right_angle_triangle(3, 4, 5) returns True, and 
    # right_angle_triangle(1, 2, 3) returns False. 
    # This function can be used to solve problems that involve right-angled triangles. 
    # For example, you could use it to determine if a triangle is a right-angled 
    # triangle, or to find the length of the third side of a right-angled triangle 
    # given the lengths of the other two sides. 
    # It is a useful tool for anyone who works with geometry or trigonometry. 
    # It is also a good example of how to use