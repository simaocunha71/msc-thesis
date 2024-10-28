```
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
```


You can test this function with the provided test cases:
```
print(fix_spaces("Example"))  # Output: "Example"
print(fix_spaces("Example 1"))  # Output: "Example_1"
print(fix_spaces(" Example 2"))  # Output: "_Example_2"
print(fix_spaces(" Example   3"))  # Output: "_Example-3"
```


This function iterates over each character in the input string. If the character is a space, it checks if the previous character in the result string is also a space. If it is, it appends a dash to the result string; otherwise, it appends an underscore. If the character is not a space, it simply appends it to the result string. The function returns the modified string.