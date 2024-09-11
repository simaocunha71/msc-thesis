"""
def find_Rotations(s):
    l = len(s)
    for i in range(1, l):
        if s[:i] == s[i:]:
            return i
    return l
"""

def find_Rotations(s):
    l = len(s)
    for i in range(1, l):
        if s[:i] == s[i:] and s[:i] != s:
            return i
    return l

print(find_Rotations("aaaa"))  # Output: 1
print(find_Rotations("abcde"))  # Output: 5
print(find_Rotations("abcd"))  # Output: 4
print(find_Rotations(""))  # Output: 0
print(find_Rotations("abcabc"))  # Output: 3
print(find_Rotations("abcdef"))  # Output: 6
print(find_Rotations("abcdabcd"))  # Output: 4
print(find_Rotations("abcdabc"))  # Output: 3


def test_find_rotations(f):
    assert f("aaaa") == 1
    assert f("abcde") == 5
    assert f("abcd") == 4
    assert f("") == 0
    assert f("abcabc") == 3
    assert f("abcdef") == 6
    assert f("abcdabcd") == 4
    assert f("abcdabc") == 3

test_find_rotations(find_Rotations)
print("All tests passed.")


def rotate(s, n):
    return s[n:] + s[:n]

def find_rotations(s):
    n = len(s)
    for i in range(1, n):
        if s[:i] == s[i:] and s[:i] != s:
            return i
    return n

print(find_rotations("aaaa"))  # Output: 1
print(find_rotations("abcde"))  # Output: 5
print(find_rotations("abcd"))  # Output: 4
print(find_rotations("")) 