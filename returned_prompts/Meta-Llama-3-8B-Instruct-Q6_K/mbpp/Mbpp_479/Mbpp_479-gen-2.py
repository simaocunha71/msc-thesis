```
def first_Digit(n):
    return int(str(n)[0])
```
This function converts the number into a string, then uses indexing to get the first character (which is the first digit). The `int()` function is used to convert this character back into an integer. 

For example, if you call `first_Digit(123)`, it will return `1`. 

Note: This function will raise an exception if the input number is less than 1. If you want to handle this case, you could add a check at the beginning of the function. For example:
```
def first_Digit(n):
    if n < 1:
        return None  # or some other default value
    return int(str(n)[0])
``` 





