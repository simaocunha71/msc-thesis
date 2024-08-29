"""
We can solve this problem by using the concept of Prefix and Suffix Arrays. 

A prefix of a string is a substring that occurs at the start of the string. Similarly, a suffix of a string is a substring that occurs at the end of the string.

A string can be rotated to get another string if and only if the concatenation of the string with itself contains the other string as a substring.

In this problem, we can check each suffix of the string by appending the string to itself and check if it contains the original string as a substring. If it does, then we can find the minimum number of rotations to get the same string.

The time complexity of this solution is O(n^2) and the space complexity is O(n).
"""

def find_Rotations(s):
    n = len(s)
    temp = s + s
    rotations = []
    
    for i in range(1, n):
        if temp[i:i+n] == s:
            rotations.append(i)
    
    min_rotations = min(rotations)
    
    return min_rotations if min_rotations < n else -1

print(find_Rotations("aaaa"))
"""

