def otherside_rightangle(base, height):
    side = (base**2 + height**2)**0.5
    return side

# Test the function
from unittest import TestCase

class TestOthersideRightangle(TestCase):

    def test_otherside_rightangle(self):
        self.assertAlmostEqual(otherside_rightangle(7,8), 10.63014581273465, places=6)

if __name__ == "__main__":
    TestOthersideRightangle()

"""
Test Cases:
1. Test if the function is correctly calculating the third side of a right angled triangle.

Explanation:
The function otherside_rightangle takes in two parameters, base and height, representing the length of the two known sides of a right angled triangle. It uses the Pythagorean theorem to calculate the length of the third side.

To test the function, the TestCase class from the unittest module is used. The TestOthersideRightangle class is defined, and a test_otherside_rightangle method is created within it. This method uses the self.assertAlmostEqual method to compare the result of the otherside_rightangle function with the expected result, which is 10.63014581273465 rounded to 6 decimal places. If the result is within the specified tolerance, the test passes. Otherwise, an AssertionError is raised.

The TestOthersideRightangle class is called within the __main__ block to execute the test cases.

Overall, this test ensures that the otherside_rightangle function correctly calculates the third side of a right angled triangle.
"""

```
```

# Python3 program to find the third side of a right angled triangle

# Function to find the third side
def otherside_rightangle(base, height):
    side = (base**2 + height**2)**0.5
    return side

# Test the function
from unittest import TestCase

class TestOthersideRightangle(TestCase):

    def test_otherside_rightangle(self):
        self.assertAlmostEqual(otherside_rightangle