
def fix_spaces(text):
    text = text.replace("  ", "-")
    text = text.replace(" ", "_")
    if text[0] == "-":
        text = text[1:]
    if text[-1] == "-":
        text = text[:-1]
    return text

print(fix_spaces("Example"))
print(fix_spaces("Example 1"))
print(fix_spaces(" Example 2"))
print(fix_spaces(" Example  3"))


# Output:
# Example
# Example_1
# _Example_2
# _Example-3

```

## Problem 2 - Count the number of words in a given text

```python
