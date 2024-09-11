def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum + 1):
        if all(num % digit == 0 for digit in str(num)):
            result.append(num)
    return result

def test_divisible_by_digits():
    assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

test_divisible_by_digits()

# Time: O(nlogn + d), d is the max length of numbers
# Space: O(1)
"""
Explanation:
The idea is to generate all numbers within [startnum, endnum] range and filter out the numbers that are not divisible by every digit.
The time complexity is dominated by the range generation, O(nlogn) since we need to generate all the numbers within range.
The space complexity is O(1) since we only use constant extra space to store the result.
"""




"""
The idea is to generate all numbers within [startnum, endnum] range and filter out the numbers that are not divisible by every digit.
The time complexity is dominated by the range generation, O(nlogn) since we need to generate all the numbers within range.
The space complexity is O(1) since we only use constant extra space to store the result.
"""



"""
Here is the code for the above solution:
"""


# Time: O(nlogn + d), d is the max length of numbers
# Space: O(1)
def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum + 1):
        if all(num % digit == 0 for digit in str(num)):
            result.append(num)
    return result

# test
def test_divisible_by_digits():
    assert divisible_by_digits(1,22)==[1, 2, 3, 