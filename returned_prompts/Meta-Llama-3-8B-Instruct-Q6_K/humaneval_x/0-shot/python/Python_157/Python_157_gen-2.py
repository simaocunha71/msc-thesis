    # Check if the sum of the squares of the two smaller sides is equal to the 
    # square of the largest side. This is a necessary condition for a triangle 
    # to be right-angled.
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else:
        return False
    # This function uses the Pythagorean theorem, which states that in a right 
    # triangle, the square of the length of the hypotenuse is equal to the sum 
    # of the squares of the lengths of the other two sides. This theorem is 
    # often written as a^2 + b^2 = c^2, where a and b are the lengths of the 
    # other two sides and c is the length of the hypotenuse. This theorem is 
    # often used to solve problems involving right triangles, such as finding the 
    # length of the hypotenuse given the lengths of the other two sides.
    # For example, if we have a right triangle with one side of length 3 and 
    # another side of length 4, we can use the theorem to find the length of 
    # the hypotenuse. We do this by squaring the lengths of the two sides and 
    # adding them together, then finding the square root of the result. This 
    # gives us the length of the hypotenuse, which is 5. This is the same 
    # result we would get if we drew the triangle and measured the length of 
    # the hypotenuse.
    # In this function, we use the theorem to check if the three sides form a 
    # right-angled triangle. We do this by checking if the sum of the squares 
    # of the two smaller sides is equal to the square of the largest side. 
    # If this is the case, we return True, indicating that the sides form a 
    # right-angled triangle. Otherwise, we return False. This function is a 
    # simple and efficient way to check if three sides form a right-angled 
    # triangle. It can be used in a variety of applications, such as in 
    # computer graphics or in geometry problems.