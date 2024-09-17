```
def first_Digit(n):
    return int(str(n)[0])
```
Explanation:
The function `first_Digit` takes an integer `n` as an argument. It converts the integer to a string using the `str()` function, then extracts the first character of the string using the `[0]` indexing. Finally, it converts the character back to an integer using the `int()` function. This way, it returns the first digit of the given number.

Example: `first_Digit(123)` returns `1`, which is the first digit of the number `123`. 