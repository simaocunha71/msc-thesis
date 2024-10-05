def fix_spaces(text):
    return text.replace("  ", "-").replace(" ", "_")

print(fix_spaces("Example"))
print(fix_spaces("Example 1"))
print(fix_spaces(" Example 2"))
print(fix_spaces(" Example   3"))