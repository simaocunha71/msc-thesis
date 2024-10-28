```
def move_num(s):
    numbers = ''
    rest = ''
    for char in s:
        if char.isdigit():
            numbers += char
        else:
            rest += char
    return rest + numbers
```


This function iterates over each character in the given string. If the character is a digit, it is added to the `numbers` string. If the character is not a digit, it is added to the `rest` string. Finally, the function returns the `rest` string followed by the `numbers` string. This effectively moves all the numbers to the end of the string. 

The unit test `assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'` helps to clarify the expected behavior of the function. It shows that all the numbers in the string should be moved to the end, regardless of their position and in the original order. 

The function passes this unit test, as it correctly moves all the numbers to the end of the string while preserving their original order. 





Note: This function does not handle the case where a single character string is passed in. It assumes that the input string will always contain at least one non-digit character. If the function should handle the case where a single character string is passed in, it would need to be modified accordingly.