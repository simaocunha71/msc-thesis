"""
def find_Rotations(s):
    """
    Find the minimum number of rotations (greater than 0)
    required to get the same string.
    """
    for i in range(len(s)):
        if s[:i] + s[i:] == s:
            return len(s) // i
    return 0

# Test
print(find_Rotations("aaaa"))
"""

# Time: O(n^2)
# Space: O(1)
def find_Rotations(s):
    for i in range(len(s)):
        if s[:i] + s[i:] == s:
            return len(s) // i
    return 0

# Test
print(find_Rotations("aaaa"))

# Time: O(n)
# Space: O(n)
def find_Rotations(s):
    s_len = len(s)
    for i in range(s_len):
        if s[:i] + s[i:] == s:
            return s_len // i
    return 0

# Test
print(find_Rotations("aaaa"))
"""

# Time: O(n)
# Space: O(n)
def find_Rotations(s):
    return len(s) if len(s) % len(s[:len(s) // 2]) == 0 else len(s) // 2

# Test
print(find_Rotations("aaaa"))
"""

# Time: O(n)
# Space: O(1)
def find_Rotations(s):
    if len(s) % 2 == 0:
        return len(s) // 2
    for i in range(len(s)):
        if s[:i] + s[i:] == s:
            return len(s) // i
    return 0

# Test
print(find_Rotations("aaaa"))
"""

# Time: O(n)
# Space: O(n)
def find_Rotations(s):
    if len(s) % 2 == 0:
        return len(s) // 2
    for i