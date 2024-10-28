def fix_spaces(text):
    # replace all spaces in the text with underscores
    text = text.replace(" ", "_")
    # find all occurrences of more than 2 consecutive underscores and replace them with -
    text = re.sub(r'_{3,}', '-', text)
    return text

# test cases
print(fix_spaces("Example"))  # Output: "Example"
print(fix_spaces("Example 1"))  # Output: "Example_1"
print(fix_spaces(" Example 2"))  # Output: "_Example_2"
print(fix_spaces(" Example   3"))  # Output: "_Example-3"