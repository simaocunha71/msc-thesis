```
def find_Max_Num(digits):
    return int(''.join(map(str, sorted(digits, reverse=True))))
```
The function `find_Max_Num` takes a list of digits as input and returns the largest number that can be formed using these digits. It does this by first sorting the digits in descending order and then joining them together to form a string. The `int` function is used to convert this string back into an integer. The result is the largest number that can be formed using the given digits. 

For example, if the input is `[1,2,3]`, the function will return `321` which is the largest number that can be formed using these digits. 

The unit test `assert find_Max_Num([1,2,3]) == 321` ensures that the function is working correctly. 

This function assumes that the input list of digits is non-empty. If the input list can be empty, the function should handle this case appropriately. 

For example, if the input is an empty list `[]`, the function could return `0` or raise an error. The choice depends on the specific requirements of the function. 

Here is an updated version of the function that handles the case where the input list is empty:
```
def find_Max_Num(digits):
    if not digits:
        return 0
    return int(''.join(map(str, sorted(digits, reverse=True))))
```
This function returns `0` if the input list is empty. You could also raise an error in this case if you prefer. For example:
```
def find_Max_Num(digits):
    if not digits:
        raise ValueError("Input list is empty")
    return int(''.join(map(str, sorted(digits, reverse=True))))
``` 














