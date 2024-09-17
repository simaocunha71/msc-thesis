import re
def find_Rotations(s):
    n = len(s)
    for i in range(n):
        if s == s[i:] + s[:i]:
            return i + 1
    return 0