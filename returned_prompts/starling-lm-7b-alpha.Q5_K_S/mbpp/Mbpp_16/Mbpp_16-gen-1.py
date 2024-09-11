"""
def text_lowercase_underscore(text):
    return any(c.islower() for c in text) and "_" in text
"""

Here's a step-by-step breakdown of the solution:

- The function `text_lowercase_underscore` takes a `text` parameter, which is the input string that we want to check.
- The `any` function is used to check if any character in the `text` string is lowercase and if an underscore is present in the `text` string.
- The `islower()` method is used to check if a character is lowercase.
- The `_` character is used to check if an underscore is present in the `text` string.
- If both conditions are met, the function will return `True`, indicating that the `text` string contains sequences of lowercase letters joined with an underscore. Otherwise, it will return `False`.

The provided code demonstrates how to use the `text_lowercase_underscore` function. It asserts that the function should return `True` for the input string `"aab_cbbbc"`.

Feel free to modify the `text_lowercase_underscore` function or use it as is to suit your specific needs.

Note: The `any` function returns `True` if at least one element in the iterable (in this case, the `text` string) satisfies the condition. If no element satisfies the condition, it returns `False`.

By using the logical `and` operator, we ensure that both conditions (lowercase letters and underscore) are met for the function to return `True`. Otherwise, it returns `False`.

Overall, this solution provides a straightforward and efficient way to check if a string contains sequences of lowercase letters joined with an underscore.

"""

# Python program to check if a string contains
# sequence of lowercase letters
# separated by an underscore

def text_lowercase_underscore(text):
    return any(c.islower() for c in text) and "_" in text

# Driver Program
print(text_lowercase_underscore("aab_cbbbc"))
print(text_lowercase_underscore("abbc"))
print(text_