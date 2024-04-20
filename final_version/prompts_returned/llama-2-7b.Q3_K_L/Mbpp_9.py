"""
Write a python function to find the minimum number of rotations (greater than 0) required to get the same string.
assert find_Rotations("aaaa") == 1
"""
# Time Complexity: O(n), where n is the length of the string input. It is done in linear time because we
# are using a binary search on a sorted array
# Space Complexity: O(1)
def find_Rotations(s):
    return find_rotation_inplace(s) - 1


def find_rotation_inplace(s):
    s = list(s)
    s.sort()
    min_index = 0 if s[0] == s[-1] else len(s) - 1
    for i in range(min_index, len(s)):
        while i >= 0 and s[i] != s[i-1]:
            i -= 1
        if i >= min_index:
            return i + 1
