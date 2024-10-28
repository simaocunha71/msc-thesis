
def fix_spaces(text):
    text = text.replace("  ", "-")
    text = text.replace(" ", "_")
    return text

print(fix_spaces("Example"))
print(fix_spaces("Example 1"))
print(fix_spaces(" Example 2"))
print(fix_spaces(" Example  3"))
<jupyter_output>
Example
Example_1
_Example_2
_Example-3
<jupyter_text>
