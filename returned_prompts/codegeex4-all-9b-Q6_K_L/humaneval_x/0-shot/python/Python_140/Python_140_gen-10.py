def fix_spaces(text):
    text = text.replace(" ", "_")
    while "__" in text:
        text = text.replace("__", "-")
    if text[0] == "_":
        text = text[1:]
    if text[-1] == "_":
        text = text[:-1]
    return text

print(fix_spaces("Example")) # "Example"
print(fix_spaces("Example 1")) # "Example_1"
print(fix_spaces(" Example 2")) # "_Example_2"
print(fix_spaces(" Example   3")) # "_Example-3"