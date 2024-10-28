
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if len(set(s[i:i + 3])) != 3:
            return False
    return True


# Testing
print(is_happy('a'))  # False
print(is_happy('aa'))  # False
print(is_happy('abcd'))  # True
print(is_happy('aabb'))  # False
print(is_happy('adb'))  # True
print(is_happy('xyy'))  # False

Output:

False
False
True
False
True
False

In this program, we first check if the string s is less than 3 characters long. If it is, we return False because a string is not happy if its length is less than 3. Then we loop over the string s and check every three consecutive characters. We convert the three characters to a set and if the length of the set is not 3, we return False because the characters are not distinct. If we don't find any such three characters, we return True because all three consecutive characters are distinct.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
