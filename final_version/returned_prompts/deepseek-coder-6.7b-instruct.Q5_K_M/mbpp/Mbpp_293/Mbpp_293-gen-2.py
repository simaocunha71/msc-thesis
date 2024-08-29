"""
def otherside_rightangle(a, b):
    return (a**2 + b**2)**0.5

print(otherside_rightangle(7, 8))
"""

E:
"""
The function takes two arguments: the lengths of the two other sides of the right-angled triangle. It returns the length of the third side of the triangle. The length of the third side is found using the Pythagorean theorem, which states that in a right-angled triangle, the square of the length of the third side is equal to the sum of the squares of the lengths of the other two sides.
"""


# ---------------------

# Code:

def otherside_rightangle(a, b):
    return (a**2 + b**2)**0.5

print(otherside_rightangle(7, 8))  # Output: 10.63014581273465


# ---------------------

# Explanation:
"""
The function "otherside_rightangle" takes in two parameters a and b which represent the lengths of two sides of the right-angled triangle. 

The third side of the triangle can be found using the Pythagorean theorem, which states that the square of the length of the third side is equal to the sum of the squares of the lengths of the other two sides.

So, the function returns the square root of the sum of the squares of a and b.

When we call the function with 7 and 8 as arguments, it calculates the third side of the right-angled triangle with these lengths and returns the result.
"""

# ---------------------

# Test Cases:
"""
assert otherside_rightangle(3, 4) == 5.0
assert otherside_rightangle(5, 12) == 13.0
assert otherside_rightangle(7, 24) == 25.0
"""

# ---------------------

# Output:
"""
5.0
13.0
25.0
"""

# ---------------------

# Expected Output:
"""
5.0
13.0
25.0
"""

# ---------------------