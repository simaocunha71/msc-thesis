def fix_spaces(text):
    text = text.replace(" ", "_")
    text = text.replace("___", "-")
    text = text.replace("__", "-")
    return text

print(fix_spaces("Example"))  # "Example"
print(fix_spaces("Example 1"))  # "Example_1"
print(fix_spaces(" Example 2"))  # "_Example_2"
print(fix_spaces(" Example   3"))  # "_Example-3"

Explanation:
The function fix_spaces takes a string as input and replaces all spaces with underscores using the replace method. Then, it replaces all consecutive underscores with a hyphen using the replace method again. Finally, it returns the modified string.