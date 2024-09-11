def divisible_by_digits(startnum, endnum):
    res = []
    for i in range(startnum, endnum + 1):
        if all(i % j == 0 for j in str(i)):
            res.append(i)
    return res

def test_divisible_by_digits():
    assert divisible_by_digits(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

test_divisible_by_digits()

# Time Complexity: O(nlog10(n))
# Space Complexity: O(1)

"""
Explanation:
- For each number between startnum and endnum, we check if it is divisible by all of its digits.
- If a number is divisible by all of its digits, then all the digits of the number must be factors of that number.
- To find the factors of a number, we can use a simple method of dividing the number by each of the numbers from 1 to the square root of the number. This is because all the factors of a number are either less than or equal to its square root.
- The time complexity of this approach is O(nlog10(n)) because we need to convert each number to a string to obtain its digits.
- The space complexity is O(1) because we are not using any extra space that grows with the size of the input.
"""

"""
Test cases:
assert divisible_by_digits(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert divisible_by_digits(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22, 33, 44, 55, 66, 77, 88, 99]
"""

"""
Corner cases: