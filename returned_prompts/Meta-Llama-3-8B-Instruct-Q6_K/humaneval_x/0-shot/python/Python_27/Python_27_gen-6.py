def flip_case(string: str) -> str:
    result = ""
    for char in string:
        if char.islower():
            result += char.upper()
        else:
            result += char.lower()
    return result
This function iterates over each character in the input string. If the character is lowercase, it converts it to uppercase using the `upper()` method. If the character is uppercase, it converts it to lowercase using the `lower()` method. The resulting string is then returned. The provided unit test `>>> flip_case('Hello') 'hELLO'` ensures that the function works correctly.