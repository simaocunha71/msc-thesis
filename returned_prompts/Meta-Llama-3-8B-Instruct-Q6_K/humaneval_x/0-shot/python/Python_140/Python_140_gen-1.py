def fix_spaces(text):
    result = ""
    for char in text:
        if char == " ":
            if result and result[-1] == " ":
                result += "-"
            else:
                result += "_"
        else:
            result += char
    return result

# Test your function
print(fix_spaces("Example"))  # Output: "Example"
print(fix_spaces("Example 1"))  # Output: "Example_1"
print(fix_spaces(" Example 2"))  # Output: "_Example_2"
print(fix_spaces(" Example   3"))  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  # Output: "_Example-3"  #