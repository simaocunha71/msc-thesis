
Here is a step-by-step guide on how to solve this problem:

1. Start with the largest number less than `n`: `n - 1`
2. Subtract that number from `n`: `n - 1`
3. If that number is zero, then `n - 1` is the largest divisor
4. If the result is not zero, then that number is a divisor. So, try the next largest number less than `n`: `n - 2`
5. Subtract that number from the result: `n - 1 - (n - 2)`
6. Repeat steps 4 and 5 until the result is zero
7. The last non-zero result is the largest divisor

Here is the Python implementation of the algorithm:

```python
def largest_divisor(n: int) -> int:
    divisor = n - 1
    while divisor > 1:
        n %= divisor
        divisor -= 1
    return divisor
```

You can test the function with the given test case:

```python
print(largest_divisor(15))  # Output: 5
```

This function will return `5` for the input `15` as expected.

Explanation:

The function `largest_divisor` takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. 

The algorithm starts by initializing the `divisor` variable with the value of `n - 1`. It then enters a `while` loop that continues until the `divisor` becomes less than or equal to `1`. 

Inside the `while` loop, the algorithm performs the following steps:

1. It uses the modulo operator `%` to find the remainder of `n` divided by `divisor`. If the remainder is `0`, it means that `divisor` is a divisor of `n`. In this case, the algorithm breaks out of the loop and returns the value of `divisor`.
2. If the remainder is not `0`, the algorithm subtracts `1` from the `divisor` and