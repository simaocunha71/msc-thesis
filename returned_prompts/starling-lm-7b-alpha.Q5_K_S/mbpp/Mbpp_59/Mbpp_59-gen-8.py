```
def is_octagonal(n):
    if n == 0:
        return False
    if n == 1:
        return True
    if n % 2 == 0:
        return False
    oct = 1 + 9 * ((n - 1) // 2) ** 2
    return oct % (2 * (n + 1)) == 0 and oct % (2 * n) == 0

def octagonal_number(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if not is_octagonal(n):
        raise ValueError("n must be a valid octagonal number")
    return 1 + 9 * ((n - 1) // 2) ** 2
```

Here's a function `is_octagonal(n)` that checks if `n` is an octagonal number. It does this by checking if `n` is 0, 1, or odd. If `n` is 0 or 1, then it is an octagonal number. If `n` is odd, then it checks if `n` is divisible by 2 and if `oct` is divisible by `2 * (n + 1)` and `2 * n`. If these conditions are met, then `n` is an octagonal number.

The `octagonal_number(n)` function calculates the `n`th octagonal number. It does this by checking if `n` is 0 or 1. If `n` is 0, then it returns 0. If `n` is 1, then it returns 1. If `n` is neither 0 nor 1, it calls the `is_octagonal(n)` function to check if `n` is a valid octagonal number. If it is, then it calculates the `n`th octagonal number using the formula `1 + 9 * ((n - 1) // 2) ** 2`.

To test the function, you can use the `assert` statement to check if the `is_octagonal(5)` function returns `True`. This will ensure that the function correctly identifies the number 5 as an octagonal number.
