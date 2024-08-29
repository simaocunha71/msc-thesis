
def find_Rotations(s: str) -> int:
    n = len(s)
    for i in range(1, n):
        if s[:i] == s[n-i:]:
            return i
    return 0

print(find_Rotations("aaaa"))

"""
In this function, we iterate over the string from 1 to n, and for each i, we check if the string s can be divided into two parts that are the same. If it can, we return the number of rotations, which is i. If no such i exists, we return 0, which means the string is already a rotation of itself.
"""

"""
