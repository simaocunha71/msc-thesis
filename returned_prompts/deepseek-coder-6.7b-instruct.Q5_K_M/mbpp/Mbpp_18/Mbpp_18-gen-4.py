def remove_dirty_chars(str1, str2):
    return ''.join([char for char in str1 if char not in str2])

print(remove_dirty_chars("probasscurve", "pros"))

"""
Here we use list comprehension to iterate over each character in the first string (str1). If the character is not found in the second string (str2), it is added to the list. Finally, we join the list of characters into a string and return it.
"""

# Test case
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
<jupyter_output>
bacuve
<jupyter_text>
**Problem 3**
<jupyter_code>
