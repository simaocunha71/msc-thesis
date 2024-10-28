The function flip_case takes a string as input and returns a new string where all lowercase characters are converted to uppercase and all uppercase characters are converted to lowercase.

Here's a Python solution for the problem:

```Python
def flip_case(string: str) -> str:
    result = ""
    for char in string:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result
```

This function iterates over each character in the input string. If the character is lowercase, it converts it to uppercase using the `upper()` method and adds it to the result string. If the character is uppercase, it converts it to lowercase using the `lower()` method and adds it to the result string. If the character is neither uppercase nor lowercase (e.g., a space or punctuation mark), it adds it to the result string as is. The function then returns the resulting string.