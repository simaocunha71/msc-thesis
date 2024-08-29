def find_length(s):
    max_diff = 0
    count_zero = 0
    count_one = 0
    for i in s:
        if i == '0':
            count_zero += 1
        else:
            count_one += 1
        diff = count_one - count_zero
        if diff > max_diff:
            max_diff = diff
    return max_diff

print(find_length("11000010001"))

"""
Explanation:
The given binary string is 11000010001.
The maximum difference between the number of 0s and 1s is 6. The sub-string is 000100.
"""

# Time Complexity: O(n)
# Space Complexity: O(1)

# Test Case 2:

