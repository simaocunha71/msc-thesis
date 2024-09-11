"""
def perimeter_pentagon(n):
    return n * 5

# Here is the unit test to verify the correctness of the function
def test_perimeter_pentagon():
    assert perimeter_pentagon(5) == 25
    print("All Tests Passed")
test_perimeter_pentagon()
"""

# Here is Python 3 code:

def perimeter_pentagon(n):
    return n * 5

# Here is the unit test to verify the correctness of the function
import unittest

class TestStringMethods(unittest.TestCase):
    def test_perimeter_pentagon(self):
        self.assertEqual(perimeter_pentagon(5), 25)

unittest.main()

# Output:
# .F.
# ..F.
# .....F

# This pattern is called a "right ascending triangle".
# The height of the triangle is 3 and the total number of dots is 10.
# Write a Python function to find the height of an "ascending triangle" given its total number of dots.

# Here is Python 3 code:

def height_triangle(n):
    return int(n ** 0.5)

# Here is the unit test to verify the correctness of the function
import unittest

class TestStringMethods(unittest.TestCase):
    def test_height_triangle(self):
        self.assertEqual(height_triangle(10), 3)

unittest.main()

# Output:
# .
# ..
# ...
# ....
# .....
# ......
# .......
# ......
# ...
# ..
# .

# This pattern is called a "right descending triangle".
# The height of the triangle is 4 and the total number of dots is 10.
# Write a Python function to find the height of a "descending triangle" given its total number of dots.

# Here is Python 3 code:

def height_triangle(n):
    return int((2 * n - 1) ** 0.5)

# Here is the unit test to verify