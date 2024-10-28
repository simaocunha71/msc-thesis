
def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
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

This function works by iterating over the string s and checking if every 3-character substring contains exactly three distinct characters. If any such substring does not have exactly three distinct characters, the function immediately returns False. If the function iterates over the entire string without finding any such substring, it returns True, indicating that the string is 'happy'.

Note: This solution assumes that the input string s consists only of lowercase letters. If the input string can contain uppercase letters or other characters, you would need to add additional error checking to handle these cases.


