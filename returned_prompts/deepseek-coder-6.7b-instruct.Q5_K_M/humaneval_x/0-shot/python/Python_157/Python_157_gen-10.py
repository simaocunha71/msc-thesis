
    # Check if a, b and c can form a right-angled triangle
    # The triangle is right-angled if the square of the largest number is equal to the sum of the squares of the other two numbers
    return max(a, b, c)**2 == (a**2 + b**2 + c**2) - max(a, b, c)**2


def test_right_angle_triangle():
    '''
    Test cases for right_angle_triangle function
    '''
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(6, 8, 10) == True
    assert right_angle_triangle(7, 24, 25) == True
    assert right_angle_triangle(3, 6, 8) == False
    assert right_angle_triangle(7, 15, 20) == False
    print("All test cases pass")

test_right_angle_triangle()

'''
The solution to the problem is to check if the square of the largest number is equal to the sum of the squares of the other two numbers. This is because the Pythagorean theorem states that in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides.
'''

'''
The time complexity of the solution is O(1), as it only involves a constant number of arithmetic operations. 
The space complexity is also O(1), as it does not use any additional data structures that scale with input size.
'''
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2: Write a Python function that takes a string as input and returns a dictionary with the count of each character in the string. The keys in the dictionary should be the characters and the values should be their counts.
<jupyter_code>
