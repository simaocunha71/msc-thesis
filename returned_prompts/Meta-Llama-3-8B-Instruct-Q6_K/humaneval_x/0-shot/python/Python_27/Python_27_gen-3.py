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


The function takes a string as input and iterates over each character in the string. If the character is lowercase, it converts it to uppercase using the `upper()` method and adds it to the result string. If the character is uppercase, it converts it to lowercase using the `lower()` method and adds it to the result string. The resulting string is then returned. 

The unit test `>>> flip_case('Hello')` is used to verify the correctness of the function. It should return the string 'hELLO', which is the result of flipping the case of the input string 'Hello'.