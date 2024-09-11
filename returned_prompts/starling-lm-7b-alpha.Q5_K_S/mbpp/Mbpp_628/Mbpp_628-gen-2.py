def replace_spaces(s):
    return s.replace(" ", "%20")

# assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'

# print(replace_spaces("My Name is Dawood"))
# print(replace_spaces("Hello World"))
# print(replace_spaces(""))
# print(replace_spaces(" "))













"""
Correct Solution:
"""

def replace_spaces(s):
    return s.replace(" ", "%20")

# assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'

# print(replace_spaces("My Name is Dawood"))
# print(replace_spaces("Hello World"))
# print(replace_spaces(""))
# print(replace_spaces(" "))

# This solution will replace all the spaces in the given string with '%20'
# and returns the modified string. It uses the built-in `replace` method in Python,
# which is used to replace occurrences of a substring in a string. In this case,
# the substring to be replaced is a space, and the replacement is '%20'.

# The `assert` statement is used to verify that the function is working correctly.
# It compares the result of the function with the expected output and checks if they are equal.

# The `print` statements are used to print the results of the function for different inputs.
# This helps in testing the function with different scenarios and checking if it is working as expected.

# The `replace_spaces` function can be used to replace spaces in any given string with '%20'.
# It can handle various scenarios, such as an empty string, a string with only spaces, and a string with a mix of characters and spaces.

# Overall, this solution provides a simple and effective way to replace spaces in a string with '%20' using the `replace` method in Python.
# It also includes some basic testing to verify the correctness of the function.
```

```

```

```
