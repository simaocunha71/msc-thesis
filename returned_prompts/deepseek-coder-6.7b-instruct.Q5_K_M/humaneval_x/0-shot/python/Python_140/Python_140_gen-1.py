
    def fix_spaces(text):
        return text.replace("  ", "-").replace(" ", "_")

    print(fix_spaces("Example"))
    print(fix_spaces("Example 1"))
    print(fix_spaces(" Example 2"))
    print(fix_spaces(" Example  3"))

Output:

    Example
    Example_1
    _Example_2
    _Example-3
    

The function `fix_spaces` uses Python's string `replace` method to replace all spaces with underscores and all double spaces with hyphens.
"""


def fix_spaces(text):
    return text.replace("  ", "-").replace(" ", "_")


print(fix_spaces("Example"))
print(fix_spaces("Example 1"))
print(fix_spaces(" Example 2"))
print(fix_spaces(" Example  3"))

# Expected output:
#
# Example
# Example_1
# _Example_2
# _Example-3
<jupyter_output>
Example
Example_1
_Example_2
_Example-3
<jupyter_text>
5. Write a Python function called `remove_duplicates` that takes a list of numbers as an argument and returns a new list with duplicate numbers removed.
<jupyter_code>
# Your code here

"""
