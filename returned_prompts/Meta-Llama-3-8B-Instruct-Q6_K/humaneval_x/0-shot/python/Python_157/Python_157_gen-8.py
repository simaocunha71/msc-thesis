    # Check if the sum of the squares of two sides is equal to the square of the third side
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else:
        return False
    # This function will check if the given sides can form a right angled triangle
    # This is based on the Pythagorean theorem which states that for a right 
    # angled triangle the square of the hypotenuse (c) is equal to the sum of 
    # squares of other two sides (a and b) i.e., c^2 = a^2 + b^2

    # The function takes three parameters a, b, c which are the sides of the triangle
    # It returns True if the sides form a right angled triangle and False otherwise

    # The function uses the if condition to check if the sum of the squares of two sides 
    # is equal to the square of the third side. If the condition is met then it returns True
    # otherwise it returns False

    # This function is a simple and efficient way to check if a triangle is right angled
    # as it only requires the lengths of the sides and does not require any trigonometric 
    # calculations or other complex operations. It is also easy to understand and 
    # implement.  It can be used in any programming language and is a good example of 
    # how mathematical concepts can be applied to programming.