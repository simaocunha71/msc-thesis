```
def is_nonagonal(n):
    if n < 1:
        return None
    return int(((9*n**2 - n) / 2))
```


The problem is asking you to write a function that finds the nth nonagonal number. Nonagonal numbers are a series of numbers that are the sum of consecutive triangular numbers. The formula for the nth nonagonal number is ((9*n**2 - n) / 2).

The unit test provided is `assert is_nonagonal(10) == 325`, which means the 10th nonagonal number is 325. We can use this to test our function.

Here's the solution:
```
def is_nonagonal(n):
    if n < 1:
        return None
    return int(((9*n**2 - n) / 2))
```


This function takes an integer `n` as input and returns the `n`th nonagonal number. If `n` is less than 1, it returns `None`. The function uses the formula ((9*n**2 - n) / 2) to calculate the `n`th nonagonal number. The result is an integer, so we use the `int()` function to convert the result to an integer.