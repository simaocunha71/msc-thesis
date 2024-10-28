def move_num(s):
    nums = []
    result = ''
    for char in s:
        if char.isdigit():
            nums.append(char)
        else:
            result += char
    return result + ''.join(nums)

# Test case
print(move_num('I1love143you55three3000thousand'))  # Output: 'Iloveyouthreethousand1143553000'  # Expected output
```
The provided unit test ensures that the function correctly moves the numbers to the end of the string. The test case is 'I1love143you55three3000thousand', which should return 'Iloveyouthreethousand1143553000'. This means that the function should correctly separate the alphanumeric characters and the numbers, and then concatenate them in the correct order.

The function works by iterating over the input string, and for each character, it checks if it is a digit using the `isdigit()` method. If the character is a digit, it is added to a list called `nums`. If the character is not a digit, it is added to the `result` string. After processing all characters, the function returns the `result` string concatenated with the `nums` list as a string.

This function correctly handles the test case and any other input string that contains alphanumeric characters and numbers. It is also efficient, as it only iterates over the input string once.  # Expected output
```
Iloveyouthreethousand1143553000
```  # Output
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
