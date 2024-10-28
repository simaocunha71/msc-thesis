```
def unique_digits(x):
    return sorted([num for num in x if all(int(digit) % 2 != 0 for digit in str(num))])
```


In this function, we use a list comprehension to filter the input list `x`. For each number `num` in `x`, we check if all its digits are odd using the `all` function and a generator expression. The `str` function is used to convert each number to a string, and then we iterate over each character (digit) in the string using a generator expression. The `int` function is used to convert each character back to an integer, and then we check if it's odd using the modulo operator `%`. If all digits are odd, we include `num` in the resulting list. Finally, we sort the resulting list in increasing order using the `sorted` function and return it.