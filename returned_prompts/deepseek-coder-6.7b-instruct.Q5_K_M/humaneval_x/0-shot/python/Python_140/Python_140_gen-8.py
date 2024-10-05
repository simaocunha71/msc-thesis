
def fix_spaces(text):
    new_text = text.replace("  ", "-")
    new_text = new_text.replace(" ", "_")
    return new_text

print(fix_spaces("Example"))
print(fix_spaces("Example 1"))
print(fix_spaces(" Example 2"))
print(fix_spaces(" Example  3"))

# Output:
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
5. Write a Python function that will take an integer n as input and return a list of the first n positive integers in descending order.The function should be named `get_descending_order`.
<jupyter_code>
