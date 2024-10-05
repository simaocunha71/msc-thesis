
def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if len(set(s[i:i+3])) != 3:
            return False
    return True

# test cases
print(is_happy('a'))  # False
print(is_happy('aa'))  # False
print(is_happy('abcd'))  # True
print(is_happy('aabb'))  # False
print(is_happy('adb'))  # True
print(is_happy('xyy'))  # False

# The function works by iterating over the string s in steps of 3, checking if the set of three consecutive letters contains exactly 3 distinct elements.
# If the set has any duplicate letters, the function returns False, indicating the string is not happy. If the function iterates over the string without finding any non-happy strings, it returns True, indicating the string is happy.
<jupyter_output>
False
False
True
False
True
False
<jupyter_text>
3. Write a Python function that takes a list of integers and returns the number of pairs that have a difference of 2.
<jupyter_code>
