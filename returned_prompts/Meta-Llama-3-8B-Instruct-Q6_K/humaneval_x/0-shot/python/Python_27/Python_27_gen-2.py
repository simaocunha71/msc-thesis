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
This function iterates over each character in the input string. If the character is lowercase, it converts it to uppercase using the `upper()` method and adds it to the result string. If the character is uppercase, it converts it to lowercase using the `lower()` method and adds it to the result string. The resulting string is then returned. 

The unit test `>>> flip_case('Hello')` checks that the function correctly flips the case of the input string. 

Note: This function does not handle non-alphabetic characters (such as digits, punctuation, or whitespace) - it will treat them as if they were letters. If you need to handle these characters differently, you would need to add additional logic to the function. 