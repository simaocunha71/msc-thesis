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


Here is an explanation of the code:

1. We initialize an empty string `result` that will store the final result.
2. We iterate over each character `char` in the input `text`.
3. If the character is a space, we check if the last character in the `result` is also a space. If it is, we append a hyphen (`-`) to the `result`. If it's not, we append an underscore (`_`) to the `result`.
4. If the character is not a space, we simply append it to the `result`.
5. Finally, we return the `result` string.

This code works by iterating over each character in the input string, and replacing spaces with either underscores or hyphens based on whether there are consecutive spaces or not. The result is a string with spaces replaced by underscores and consecutive spaces replaced by hyphens.