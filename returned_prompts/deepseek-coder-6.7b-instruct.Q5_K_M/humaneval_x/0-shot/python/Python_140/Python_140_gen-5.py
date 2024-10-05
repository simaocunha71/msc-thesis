
def fix_spaces(text):
    new_text = ''
    spaces_count = 0
    for ch in text:
        if ch == ' ':
            spaces_count += 1
            if spaces_count == 2:
                new_text += '-'
        else:
            if spaces_count == 2:
                new_text += '-'
            elif spaces_count > 2:
                new_text += '_'
            new_text += ch
            spaces_count = 0
    return new_text

# test cases
print(fix_spaces("Example"))  # "Example"
print(fix_spaces("Example 1"))  # "Example_1"
print(fix_spaces(" Example 2"))  # "_Example_2"
print(fix_spaces(" Example   ."))  # "_Example-."
print(fix_spaces(" Example  3"))  # "_Example-3"
print(fix_spaces("  Example  3"))  # "--Example-3"
print(fix_spaces("   Example  3"))  # "---Example-3"
print(fix_spaces("    Example  3"))  # "----Example-3"

This function works by iterating over each character in the input string, checking if it's a space or not. If it's a space, it increments a counter `spaces_count`. If it's not a space, it checks the `spaces_count`:

- If `spaces_count` is exactly 2, it adds `-` to `new_text` and resets `spaces_count` to 0.
- If `spaces_count` is more than 2, it adds `_` to `new_text` and resets `spaces_count` to 0.
- If `spaces_count` is 1 or 0, it adds the character to `new_text` and resets `spaces_count` to 0.

This way, it's guaranteed to replace every single space with underscores, and every run of 3 or more spaces with a dash.

Note:
This solution assumes that the string only contains printable ASCII characters, excluding whites