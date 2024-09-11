```
def closest_num(n):
    for i in range(n-1, 0, -1):
        if i <= n:
            return i
```

Explanation:

The function `closest_num` takes an integer `n` as input and iterates from `n-1` down to `1` in steps of `-1`. It checks if the current value of `i` is less than or equal to `n`, and if so, it returns `i` as the closest smaller number to `n`. 

For example, when `closest_num(11)` is called, it will iterate through the numbers `10`, `9`, `8`, `7`, `6`, `5`, `4`, `3`, `2`, and `1`. Since `10` is the first number that is less than or equal to `11`, it will return `10` as the closest smaller number to `11`. 

This solution effectively finds the closest smaller number by continuously decrementing the value of `i` until it finds a number that is less than or equal to the input `n`. 

Note: The function assumes that the input `n` is a positive integer. If negative numbers are allowed as input, additional checks and handling may be necessary.

Overall, this function provides a simple and efficient solution to find the closest smaller number to a given input.

```python
def closest_num(n):
    for i in range(n-1, 0, -1):
        if i <= n:
            return i
```

You can use this function by calling it with a positive integer argument, like `closest_num(11)`, and it will return the closest smaller number to the input.

For example, if you call `closest_num(11)`, it will return `10` as the closest smaller number to `11`. 

Please note that the function assumes that the input `n` is a positive integer. If negative numbers are allowed as input, additional checks and handling may be necessary.
```python
def closest_num(n):
    for i in range(n-1, 0, -1):
        if i <= n:
            return i
