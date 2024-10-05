def fix_spaces(text):
    text = text.replace(" ", "_")
    text = re.sub(r"_+", "-", text)
    return text

print(fix_spaces("Example"))
print(fix_spaces("Example 1"))
print(fix_spaces(" Example 2"))
print(fix_spaces(" Example   3"))