"""
def armstrong_number(n):
    num_str = str(n)
    length = len(num_str)
    sum = 0
    for i in num_str:
        sum += int(i) ** length
    if sum == n:
        return True
    else:
        return False
"""

import math

def armstrong_number(n):
    num_str = str(n)
    length = len(num_str)
    sum = 0
    for i in num_str:
        sum += int(i) ** length
    if sum == n:
        return True
    else:
        return False

def test_armstrong_number():
    assert armstrong_number(153) == True
    assert armstrong_number(370) == True
    assert armstrong_number(371) == False
    assert armstrong_number(9474) == True
    assert armstrong_number(100) == False

test_armstrong_number()

# Created by: Raghib Sheikh
# Date: 12/09/2020

"""
In computer science, an armstrong number, A-number, or n-dimensional heteroclito, is a number that is the sum of its own digits each raised to the power of the number of digits. For example, 371 is an armstrong number, because 3 * 3 * 3 + 7 * 7 * 7 + 1 * 1 * 1 is 343 + 343 + 1, which is 687.
"""

"""
The sum of the cubes of the digits is equal to the number itself. For example, 153 is an armstrong number because 1 * 1 * 1 + 5 * 5 * 5 + 3 * 3 * 3 equals 1 + 125 + 27 = 153.
"""

"""
For example:
armstrong_number(153) # True
armstrong_number(370) # True
armstrong_number(371) # False
armstrong_number(