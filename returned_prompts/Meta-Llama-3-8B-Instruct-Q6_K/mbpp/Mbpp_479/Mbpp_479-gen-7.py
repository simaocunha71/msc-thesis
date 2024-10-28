```
def first_Digit(n):
    return int(str(n)[0])
```
This function converts the number to a string and then returns the first character of the string as an integer. This is equivalent to finding the first digit of the number. The unit test `assert first_Digit(123) == 1` ensures that the function returns the correct result.