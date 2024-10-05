
Let's break down the problem into smaller cases:

1. If both `x` and `y` are even, the biggest even integer in the range is the smaller of the two.
2. If `x` is even and `y` is odd, the biggest even integer in the range is `x` if `x` is less than or equal to `y`, otherwise it's -1.
3. If `x` is odd and `y` is even, the biggest even integer in the range is `y`.
4. If both `x` and `y` are odd, there is no even integer in the range, so the function should return -1.

Here's the Python code that implements these cases:
```
def choose_num(x, y):
    if x % 2 == 0:
        if y % 2 == 0:
            return min(x, y)
        else:
            return x if x <= y else -1
    else:
        if y % 2 == 0:
            return y
        else:
            return -1
```
This code uses the modulo operator (`%`) to check if a number is even or odd, and the `min` function to find the smaller of two numbers. The `if` statements are used to implement the different cases. The function returns the biggest even integer in the range, or -1 if there is no such integer.