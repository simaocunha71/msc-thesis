```
def flip_case(string: str) -> str:
    result = ""
    for char in string:
        if char.islower():
            result += char.upper()
        else:
            result += char.lower()
    return result
```
This function iterates over each character in the input string. If the character is lowercase, it converts it to uppercase using the `upper()` method, and if it's uppercase, it converts it to lowercase using the `lower()` method. The resulting string is then returned. The test case `flip_case('Hello')` demonstrates the function's behavior, which is to flip the case of the input string. For example, 'Hello' becomes 'hELLO'.