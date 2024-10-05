
def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if len(set(s[i:i + 3])) != 3:
            return False
    return True

print(is_happy('a')) # False
print(is_happy('aa')) # False
print(is_happy('abcd')) # True
print(is_happy('aabb')) # False
print(is_happy('adb')) # True
print(is_happy('xyy')) # False



"""
This function works by iterating over the string s in steps of 3 (using the range function). 
For each group of 3 letters, it converts the group to a set. 
A set is a data type in Python that does not allow duplicate elements. 
So, if the length of the set is not 3, it means that the 3 letters are not distinct, and the function returns False.
If the function has iterated over the entire string without returning False, it means that all groups of 3 letters were distinct, and the function returns True.
"""
<jupyter_output>
False
False
True
False
True
False
<jupyter_text>
2. Write a Python function that can take a list of strings and return a dictionary where the keys are the unique letters in the strings and the values are the counts of these letters.
<jupyter_code>
