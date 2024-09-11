from math import sqrt
def otherside_rightangle(a, b):
    c = sqrt(a*a + b*b)
    return c

# Call the function and pass arguments
print(otherside_rightangle(7,8))


"""
Explanation:
In a right angle triangle, the square of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the other two sides.
This is represented by the Pythagorean theorem: a² + b² = c².
The theorem is named after the ancient Greek mathematician Pythagoras, who is traditionally credited with its discovery, although evidence exists of earlier discoveries.

In this problem, we need to calculate the third side of a right angle triangle given two sides.
We can use the Pythagorean theorem to calculate the third side.
We can use the sqrt function from the math module to calculate the square root of the sum of the squares of the two sides.
The function takes two arguments, the lengths of the two sides of the triangle, and returns the length of the third side.
"""

"""
Test Case:
When we run the code with the test case otherside_rightangle(7,8), the function will return 10.63014581273465, which is the length of the third side of the right angle triangle.
"""

"""
Time Complexity:
The time complexity of this function is O(1) because it performs a single square root operation and a single addition operation, both of which have a constant time complexity.
"""

"""
Space Complexity:
The space complexity of this function is O(1) because it uses a single variable, c, to store the result, and a single variable for the square root operation.
Both of these variables require a fixed amount of space, regardless of the size of the input.
"""

"""
Further Optimization:
The given function is already optimized as it uses the sqrt function from the math module to calculate the square root of the sum of the squares of the two sides, which is the most efficient way to calculate the square root in Python.
There are no additional optimizations that can be made to improve the time