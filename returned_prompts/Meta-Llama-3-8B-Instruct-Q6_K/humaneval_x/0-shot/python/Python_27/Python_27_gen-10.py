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
Explanation:
This function takes a string as input and returns a new string where all lowercase characters are converted to uppercase and all uppercase characters are converted to lowercase.

The function iterates over each character in the input string using a for loop. For each character, it checks if the character is lowercase using the `islower()` method. If the character is lowercase, it converts it to uppercase using the `upper()` method and adds it to the result string. If the character is uppercase, it converts it to lowercase using the `lower()` method and adds it to the result string.

Finally, the function returns the resulting string. The time complexity of this function is O(n), where n is the length of the input string, because it needs to iterate over each character in the string once. The space complexity is also O(n), because it needs to create a new string to store the result.