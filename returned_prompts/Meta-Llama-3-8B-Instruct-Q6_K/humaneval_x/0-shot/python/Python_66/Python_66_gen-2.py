```
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
```


This function uses a generator expression to iterate over each character `c` in the input string `s`. The `isupper()` method is used to check if the character is an uppercase letter, and if it is, the `ord()` function is used to get its ASCII code. The `sum()` function is then used to add up all the ASCII codes of the uppercase characters. If the input string is empty, the function will return 0.