
def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(0, len(s) - 2):
        if len(set(s[i:i+3])) != 3:
            return False
    return True

# Test cases
print(is_happy('a'))  # False
print(is_happy('aa'))  # False
print(is_happy('abcd'))  # True
print(is_happy('aabb'))  # False
print(is_happy('adb'))  # True
print(is_happy('xyy'))  # False

This solution works by iterating over each 3-character substring in the string and checking if all characters are distinct by converting the substring to a set (which automatically removes duplicates). If any 3-character substring does not have all distinct characters, the function returns False. If all 3-character substrings have all distinct characters, the function returns True.

The time complexity of this solution is O(n), where n is the length of the string. This is because we iterate over every character in the string once.
"""

# Test cases
print(is_happy('a'))  # False
print(is_happy('aa'))  # False
print(is_happy('abcd'))  # True
print(is_happy('aabb'))  # False
print(is_happy('adb'))  # True
print(is_happy('xyy'))  # False
<jupyter_output>
False
False
True
False
True
False
<jupyter_text>
