Here is one way you can define the function:

```python
def first_Digit(n):
    while n >= 10:
        n //= 10
    return n
```

Here's how the function works:

- It takes a single integer argument, `n`.
- The function enters a while loop that continues as long as `n` is greater than or equal to 10.
- Inside the loop, we perform an integer division of `n` by 10 and assign the result back to `n`. This effectively removes the last digit from `n`.
- When the loop ends, `n` will be the original number without its last digit, so we return `n`.

The function will return the first digit of the given number.

For example, if you call `first_Digit(123)`, it will return `1`, as the first digit of 123 is 1.

Note that this function assumes the input will always be a positive integer. If you want to handle other cases, you can add appropriate error handling.

```python
def first_Digit(n):
    try:
        while n >= 10:
            n //= 10
        return n
    except TypeError:
        print("Invalid input. Please enter a positive integer.")
```

This version of the function will raise a `TypeError` if the input is not a positive integer.

```python
def first_Digit(n):
    if isinstance(n, int) and n >= 0:
        while n >= 10:
            n //= 10
        return n
    else:
        print("Invalid input. Please enter a positive integer.")
```

This version uses the `isinstance()` function to check if the input is an integer and if it's non-negative. If the input is valid, the function proceeds as before. If the input is invalid, it prints an error message.

```python
def first_Digit(n):
    if not isinstance(n, int):
        print("Invalid input. Please enter an integer.")
        return None
    if n < 0:
        print("Invalid input. Please enter a non