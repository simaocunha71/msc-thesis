```
def fix_spaces(text):
    result = ""
    for char in text:
        if char == " ":
            if result[-1] == " ":
                result += "-"
            else:
                result += "_"
        else:
            result += char
    return result
```


The function `fix_spaces` iterates over each character in the input string. If the character is a space, it checks if the last character in the result string is also a space. If it is, it appends a hyphen to the result string; otherwise, it appends an underscore. If the character is not a space, it simply appends the character to the result string. The function returns the resulting string.