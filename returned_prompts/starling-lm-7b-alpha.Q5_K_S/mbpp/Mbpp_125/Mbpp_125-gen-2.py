"""
def find_length(s):
    n = len(s)
    max_length = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            zeros = s[i:j].count('0')
            ones = s[i:j].count('1')
            length = max(zeros, ones) - min(zeros, ones)
            max_length = max(max_length, length)
    return max_length
"""

def find_length(s):
    n = len(s)
    max_length = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            zeros = s[i:j].count('0')
            ones = s[i:j].count('1')
            length = max(zeros, ones) - min(zeros, ones)
            max_length = max(max_length, length)
    return max_length

def test():
    assert find_length("11000010001") == 6
    assert find_length("01000000101") == 6
    assert find_length("11001010011") == 3
    print("All tests passed.")

test()

"""
"""
"""

A binary string is a string consisting of only the characters '0' and '1'.
In this problem, we need to find the maximum difference between the number of 0s and the number of 1s in any sub-string of the given binary string.
To solve this problem, we can iterate through all possible sub-strings of the given binary string and count the number of 0s and 1s in each sub-string. Then, we can calculate the maximum difference between the number of 0s and the number of 1s in each sub-string. Finally, we return the maximum difference.

In the provided Python function find_length(s), we first initialize the maximum length to 0. Then, we iterate through all possible sub-strings of the given binary string s. For each sub-string, we count the