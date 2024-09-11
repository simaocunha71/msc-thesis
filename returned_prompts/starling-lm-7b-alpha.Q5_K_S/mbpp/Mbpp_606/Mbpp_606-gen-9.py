"""
def radian_degree(degrees):
    return degrees*math.pi/180

def test_radian_degree():
    assert radian_degree(90)==1.5707963267948966, "Test Failed"
    print("Test Passed")

test_radian_degree()
"""

import math

def radian_degree(degrees):
    return degrees*math.pi/180

def test_radian_degree():
    assert radian_degree(90)==1.5707963267948966, "Test Failed"
    print("Test Passed")

test_radian_degree()




"""
def radian_degree(degrees):
    radians = (degrees*math.pi)/180
    return radians

def test_radian_degree():
    assert radian_degree(90)==1.5707963267948966, "Test Failed"
    print("Test Passed")

test_radian_degree()
"""

```

Answer:
The function `radian_degree` takes in a number of degrees and returns the equivalent value in radians. The conversion is done by multiplying the degrees by pi and dividing by 180. In the provided test case, the function is called with the argument 90 and the expected output is 1.5707963267948966. The `test_radian_degree` function is used to verify that the output of `radian_degree` is correct by comparing it to the expected value. If the output is correct, the test passes and the message "Test Passed" is printed. Otherwise, the test fails.

To verify the correctness of the function, you can add additional test cases by modifying the `test_radian_degree` function and adding more assertions. For example, you can test the function with different inputs such as 45, 180, and 360 to ensure that it produces the correct results for those cases as well.
