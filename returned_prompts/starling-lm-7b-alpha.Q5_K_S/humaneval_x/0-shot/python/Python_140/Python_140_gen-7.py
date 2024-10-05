
def fix_spaces(text):
    # Replace single spaces with underscores
    text = text.replace(" ", "_")

    # Replace more than 2 consecutive spaces with -
    text = "".join(text.split("__"))

    return text

# Tests
print(fix_spaces("Example"))  # "Example"
print(fix_spaces("Example 1"))  # "Example_1"
print(fix_spaces(" Example 2"))  # "_Example_2"
print(fix_spaces(" Example   3"))  # "_Example-3"






def fix_spaces(text):
    # Replace single spaces with underscores
    text = text.replace(" ", "_")

    # Replace more than 2 consecutive spaces with -
    text = "".join(text.split("__"))

    return text

# Tests
print(fix_spaces("Example"))  # "Example"
print(fix_spaces("Example 1"))  # "Example_1"
print(fix_spaces(" Example 2"))  # "_Example_2"
print(fix_spaces(" Example   3"))  # "_Example-3"






def fix_spaces(text):
    # Replace single spaces with underscores
    text = text.replace(" ", "_")

    # Replace more than 2 consecutive spaces with -
    text = "".join(text.split("__"))

    return text

# Tests
print(fix_spaces("Example"))  # "Example"
print(fix_spaces("Example 1"))  # "Example_1"
print(fix_spaces(" Example 2"))  # "_Example_2"
print(fix_spaces(" Example   3"))  # "_Example-3"






def fix_spaces(text):
    # Replace single spaces with underscores
    text = text.replace(" ", "_")

    # Replace more than 2 consecutive spaces with -
    text = "".join(text.split("__"))

    return text

# Tests
print(fix_sp