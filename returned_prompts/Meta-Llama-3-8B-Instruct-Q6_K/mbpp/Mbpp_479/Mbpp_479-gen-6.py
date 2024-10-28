You can use the built-in Python function int() to convert the number to a string, and then use indexing to get the first digit. Here's how you can do it:

```
def first_Digit(n):
    return int(str(n)[0])
```
This function takes an integer n as input, converts it to a string, and then returns the first character of the string (which is the first digit of the number). The unit test `assert first_Digit(123) == 1` ensures that the function works correctly. 

Please note that the input number is considered as a positive integer. If the number is negative, you need to handle it separately. Also, if the number is less than 10, it is considered as a single digit number. If you want to handle these cases differently, you can add additional conditions in the function. 