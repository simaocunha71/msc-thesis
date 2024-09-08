"""
We will use python built-in function replace() to replace the characters in the first string which are present in the second string with empty string.
"""

def remove_dirty_chars(string1, string2):
    for char in string2:
        string1 = string1.replace(char, '')
    return string1

print(remove_dirty_chars("probasscurve", "pros"))  # 'bacuve'


# Another approach using list comprehension and join()
def remove_dirty_chars(string1, string2):
    return ''.join([char for char in string1 if char not in string2])

print(remove_dirty_chars("probasscurve", "pros"))  # 'bacuve'

