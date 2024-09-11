def otherside_rightangle(a,b):
    c=((a**2)+(b**2))**0.5
    return c

# Your code should go here

def test_otherside_rightangle():
    assert otherside_rightangle(7,8)==10.63014581273465
    print('All tests passed')

test_otherside_rightangle()

"""
Write a function to find the third side of a right angled triangle.
The formula to calculate the third side of a right angled triangle is c=sqrt(a^2+b^2), where c is the third side, a and b are the other two sides of the triangle.
"""

"""
In this problem, we need to write a function to calculate the third side of a right angled triangle. The input to the function should be the lengths of the other two sides of the triangle, and the function should return the length of the third side.
The formula to calculate the third side of a right angled triangle is c=sqrt(a^2+b^2), where c is the third side, a and b are the other two sides of the triangle.
We can use this formula to calculate the third side of the triangle.
"""

"""
In this problem, we are given the lengths of two sides of a right angled triangle, and we need to calculate the length of the third side of the triangle. We can use the Pythagorean theorem to calculate the length of the third side. The Pythagorean theorem states that in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides.
We can write a function that takes the lengths of the other two sides of the triangle as input and returns the length of the third side. The function can use the Pythagorean theorem to calculate the length of the third side.
"""

"""
In this problem, we are given the lengths of two sides of a right angled triangle, and we need to calculate the length of the third side of the triangle. We can use the Pythagorean theorem to calculate the length of the third side. The Pythagorean theorem