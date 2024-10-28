```
def last_Digit(n):
    return int(str(n)[-1])
```


This function works by first converting the number to a string, then using Python's string slicing feature to get the last character of the string. The `[-1]` index in Python refers to the last item in a list or string. Finally, we convert the string character back to an integer using `int()`. This function will work for any positive integer input.  It does not handle negative numbers or non-integer inputs.